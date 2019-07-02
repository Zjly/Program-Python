import pymysql
import requests
import json


def get_course_data(url):
	web_data = requests.get(url).text
	data = json.loads(web_data)

	course_id = data["number"]
	course_name = data["name"]
	course_teacher = data["teacher"]
	course_type = data["field"]
	course_school = "武汉大学"
	course_college = data["academy"]
	course_introduce = data["summary"]


def get_course_comments(url):
	web_data = requests.get(url).text
	data = json.loads(web_data)

	comments = data["comment"]
	comments_list = []
	for c in comments:
		comment = [c["student"]["name"], c["score"]["quality"], c["content"], c["time"]]
		comments_list.append(comment)

	return comments_list


def write_to_database(course_id, list):
	db = pymysql.connect("localhost", "root", "root", "test")
	cursor = db.cursor()
	for comment in list:
		sql = "INSERT INTO cm_comment(course_id, student_name, comment_quality, comment_content, comment_time) VALUES ('%s', '%s', '%s', '%s', '%s')" % (
			course_id, comment[0], comment[1], comment[2], comment[3])
		cursor.execute(sql)

	try:
		db.commit()
	except:
		db.rollback()

	db.close()


if __name__ == '__main__':
	get_course_data("https://taoke.ziqiang.net.cn/api/course/public/elective/20182022196/")
	comments = get_course_comments(
		"https://taoke.ziqiang.net.cn/api/course/public/elective/20182022196/comment/?page=1&per_page=10")
	write_to_database("20182022196", comments)
