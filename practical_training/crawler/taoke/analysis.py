import json
import re
from datetime import datetime

import pymysql
import requests

db = pymysql.connect("localhost", "root", "root", "test")
# db = pymysql.connect(host="cdb-5oviul9n.gz.tencentcdb.com", port=10094, user="root", passwd="Ab123123",
# 					 db="class_manage")
cursor = db.cursor()


def choose_analysis():
	"""
	对网页进行分析
	:return: 所有课程的课程号list
	"""
	# 读取选课信息网页
	with open("taokela.txt", 'r', encoding='UTF-8') as f:
		html = f.read()

	# 获取每门课程课程号
	pattern = "<a _v-7b0463a8=\"\" href=\"#!/course/public/elective/(.*?)\">"
	p = re.compile(pattern, re.S)
	course_number_list = p.findall(html)

	return course_number_list


def analysis_data(course_number_list):
	"""
	对每个课程号进行处理
	:param course_number_list: 课程号list
	:return:
	"""
	course_list = []
	c_comments_list = []

	for course_number in course_number_list:
		# 得到课程信息和课程评论url
		course_data_url = f"https://taoke.ziqiang.net.cn/api/course/public/elective/{course_number}/"
		course_comments_url = f"https://taoke.ziqiang.net.cn/api/course/public/elective/{course_number}/comment/?page=1&per_page=1000"

		# 得到课程信息和课程评论list
		course = get_course(course_data_url)
		comments = get_course_comments(course_comments_url)

		course_list.append(course)
		c_comments = [course[0], comments]
		c_comments_list.append(c_comments)

	# 将他们写入数据库
	write_course_database(course_list)
	write_comment_database(c_comments_list)


def save_comments(c_comments_list):
	"""
	保存评论list到csv文件中
	:param c_comments_list:
	:return:
	"""
	with open("comments.csv", "w", encoding="utf-8") as fp:
		for comments in c_comments_list:
			for comment in comments[1]:
				fp.write(str(comments[0]) + "|")
				for j in range(4):
					fp.write(comment[j].replace("\n", ""))
					if j != 3:
						fp.write("|")
				fp.write("\n")


def get_course(url):
	"""
	得到课程信息
	:param url: 课程信息url
	:return:课程信息
	"""
	web_data = requests.get(url).text
	data = json.loads(web_data)

	course = [data["number"], data["name"], data["teacher"], data["field"], "武汉大学", data["academy"], data["summary"]]
	return course


def get_course_comments(url):
	"""
	得到课程评论
	:param url: 课程评论url
	:return: 课程评论list
	"""
	web_data = requests.get(url).text
	data = json.loads(web_data)

	comments = data["comment"]
	comments_list = []
	for c in comments:
		comment = [c["student"]["name"], c["score"]["quality"], c["content"], c["time"]]
		comments_list.append(comment)

	return comments_list


def write_course_database(course_list):
	"""
	将课程信息写入数据库
	:param course: 课程信息
	:return:
	"""
	for course in course_list:
		# 查找这个老师是否存在
		teacher_name = course[2]
		sql_teacher = "SELECT tID FROM CM_teacher WHERE teacher_name = \'%s\'" % (teacher_name)
		cursor.execute(sql_teacher)
		results = cursor.fetchall()

		# 若老师不存在则插入老师
		if len(results) == 0:
			insert_teacher_sql = "INSERT INTO CM_teacher(teacher_name, teacher_introduce, teacher_totalScore) VALUES ('%s', '%s', '%s')" % (
				course[2], "", "")
			cursor.execute(insert_teacher_sql)

			# 得到新插入老师的id
			sql_teacher = "SELECT tID FROM CM_teacher WHERE teacher_name = \'%s\'" % (teacher_name)
			cursor.execute(sql_teacher)
			results = cursor.fetchall()

		tID_this_course = results[0][0]

		# 插入课程
		insert_course_sql = "INSERT INTO CM_course(tID, course_id, course_name, course_type, course_student_count, course_school, course_college, course_introduce, course_score) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
			tID_this_course, course[0], course[1], course[3], 0, "武汉大学", course[5], course[6], 0)

		# 执行sql语句
		cursor.execute(insert_course_sql)

	try:
		db.commit()
	except:
		db.rollback()


def write_comment_database(c_comments_list):
	"""
	将评论写入数据库
	:param c_comments_list: 课程评论list
	:return:
	"""
	for comments_list in c_comments_list:
		# 对该课程的每一条评论进行插入
		for comment in comments_list[1]:
			comment_content = comment[2].replace("\'", "")
			comment_sql = "INSERT INTO CM_comment(course_id, student_name, comment_quality, comment_content, comment_time) VALUES ('%s', '%s', '%s', '%s', '%s')" % (
				comments_list[0], comment[0], comment[1], comment_content, comment[3])
			cursor.execute(comment_sql)

	try:
		db.commit()
	except:
		db.rollback()


def clear_database():
	"""
	清空相关数据库内内容
	:return:
	"""
	truncate_sql1 = "TRUNCATE TABLE CM_teacher"
	truncate_sql2 = "TRUNCATE TABLE CM_course"
	truncate_sql3 = "TRUNCATE TABLE CM_comment"
	cursor.execute(truncate_sql1)
	cursor.execute(truncate_sql2)
	cursor.execute(truncate_sql3)

	try:
		db.commit()
	except:
		db.rollback()


if __name__ == '__main__':
	start_time = datetime.now()
	print("start time: " + str(start_time))

	clear_database()
	data = choose_analysis()
	analysis_data(data)
	db.close()

	end_time = datetime.now()
	print("end time: " + str(end_time))
	print("total time: " + str(end_time - start_time))
