import re
import pymysql


def choose_analysis():
	"""
	从所获取的选课表中提取出课程信息存储在list中
	:return: 课程信息总list，list中的每一条目是存储一门课程信息的list
	"""
	# 读取选课信息网页
	with open("choose_page.html", 'r') as f:
		info = f.read()

	# 分隔匹配每门课程
	pattern = "<tr >(.*?)<div class="
	p = re.compile(pattern, re.S)
	course = p.findall(info)

	# 存储所有课程信息
	array = []
	for c in course:
		# 储存单门课程中不同字段的信息
		line = []

		# 匹配课程名
		pattern_name = "<td  style=\" word-wrap:break-word;\">(.*?)</td>"
		p = re.compile(pattern_name, re.S)
		name = p.findall(c)
		line.append(name[0])

		# 匹配课程信息
		pattern_data = "(<td>|<td >)(.*?)</td>"
		p = re.compile(pattern_data, re.S)
		data = p.findall(c)
		for d in data:
			# 忽略选课人数
			if d[1].find("<font color=\"#FF0000\">") >= 0:
				continue
			line.append(d[1])

		array.append(line)

	return array


def write_to_database_course(array):
	"""
	将分析得到的数据存入本地数据库中
	:param array: 课程数据总list
	:return:
	"""
	# 连接数据库
	# db = pymysql.connect("localhost", "root", "root", "class")
	db = pymysql.connect(host="cdb-5oviul9n.gz.tencentcdb.com", port=10094, user="root", passwd="Ab123123",
						 db="WHU_course")

	# 获取操作游标
	cursor = db.cursor()

	# 课程ID和教师ID
	cID = 1
	tID = 1

	# 清空表内原本数据
	truncate_sql1 = "TRUNCATE TABLE cm_teacher"
	truncate_sql2 = "TRUNCATE TABLE cm_course"
	cursor.execute(truncate_sql1)
	cursor.execute(truncate_sql2)

	# 遍历其中的每一条课程信息
	for course in array:
		# 查询老师是否已经存在
		tName = course[2]
		sql_teacher = "SELECT tID FROM cm_teacher WHERE teacher_name = \'%s\'" % (tName)
		cursor.execute(sql_teacher)
		results = cursor.fetchall()

		# 老师不存在则新增老师
		if len(results) == 0:
			tID_this_course = tID
			# 插入老师
			sql1 = "INSERT INTO cm_teacher VALUES ('%s', '%s', '%s', '%s')" % (tID, course[2], "", "")
			cursor.execute(sql1)
			tID = tID + 1
		# 老师存在则将当前课程的tID设置为老师tID
		else:
			tID_this_course = results[0][0]

		# 插入课程
		sql2 = "INSERT INTO cm_course VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
			cID, tID_this_course, cID, course[0], course[5], 0, "武汉大学", course[4], "", 0)

		# 执行sql语句
		cursor.execute(sql2)

		cID = cID + 1

	try:
		# 提交到数据库执行
		db.commit()
	except:
		# 如果发生错误则回滚
		db.rollback()

	# 关闭数据库连接
	db.close()


if __name__ == '__main__':
	course_array = choose_analysis()
	write_to_database_course(course_array)
