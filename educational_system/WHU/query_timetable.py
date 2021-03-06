import re
from urllib import request

from educational_system.WHU.login import get_login_opener


def get_timetable(opener, year, term):
	timetable_url = f"http://218.197.150.140/servlet/Svlt_QueryStuLsn?csrftoken=a68bf89f-596c-38b0-b7c0-2503fb425b28&action=normalLsn&year={year}&term={term}&state="
	res = opener.open(request.Request(timetable_url))
	return res.read().decode("gbk")


def get_courses_range(data):
	"""
	从网页源代码中匹配出课程信息部分
	:param data: 网页源代码
	:return: 分隔为每一门课的，包含有课程信息的网页源代码list
	"""
	pattern = "<tr>(.*?)</tr>"
	p = re.compile(pattern, re.S)
	courses_range = p.findall(data)
	# 第一项为列标题故删去
	courses_range.pop(0)
	return courses_range


def get_course_list(courses_range):
	"""
	得到包含课程表信息的list
	:param courses_range: 包含课程信息范围源代码的list
	:return: 包含课程表信息的list 构成为：课程号，课程名，教师，课程时间
	"""
	course_list = []
	for course_range in courses_range:
		# 匹配课程信息
		pattern = "<td>(.*?)</td>"
		p = re.compile(pattern, re.S)
		course_data = p.findall(course_range)
		for i in range(len(course_data)):
			course_data[i] = course_data[i].replace("\t", "").replace("\n", "").replace(" ", "").replace("\r", "")
		course_id = course_data[0]
		course_name = course_data[1][0:course_data[1].index("<")]
		course_teacher = course_data[5]

		# 匹配课程时间
		pattern = "<td id='' title='<div>(.*?)<br/>"
		p = re.compile(pattern, re.S)
		time = p.findall(course_range)
		course_time = time[0].replace("\t", "").replace("\n", "").replace(" ", "").replace("\r", "")

		course = [course_id, course_name, course_teacher, course_time]
		course_list.append(course)
	return course_list


def display_timetable_data(course_list):
	"""
	显示课程表信息
	:param course_list:
	:return:
	"""
	for course in course_list:
		print(course)


if __name__ == '__main__':
	user_id = input("用户名: ")
	password = input("密码: ")
	login_opener = get_login_opener(user_id, password)
	timetable_data = get_timetable(login_opener, 2019, 1)
	ranges = get_courses_range(timetable_data)
	courses = get_course_list(ranges)
	display_timetable_data(courses)
