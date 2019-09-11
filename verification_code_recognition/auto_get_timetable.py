import re
import hashlib
from io import BytesIO
from urllib import parse
from urllib import request
from http.cookiejar import CookieJar
import PIL.Image
import cv2
import numpy

from verification_code_recognition.image_recognition import image_recognition_from_web

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}


def get_opener():
	"""
	获取opener对象，存有cookies
	:return:
	"""
	cookieJar = CookieJar()
	handler = request.HTTPCookieProcessor(cookieJar)
	opener = request.build_opener(handler)

	return opener


def login(opener, id, password):
	"""
	发送账号密码验证码，登录教务系统
	:param opener:
	:return:
	"""
	login_url = 'http://218.197.150.140/servlet/Login'
	opener.open(request.Request(login_url))

	# 验证码
	img_url = 'http://218.197.150.140//servlet/GenImg'
	res = opener.open(request.Request(img_url))
	tempIm = BytesIO(res.read())
	im = PIL.Image.open(tempIm)

	# 将验证码转为opencv图片格式
	img = cv2.cvtColor(numpy.array(im), cv2.COLOR_RGB2BGR)
	# 调用函数识别验证码
	yzm = image_recognition_from_web(img)

	# post的参数
	post_data = parse.urlencode({
		'id': id,
		'pwd': hashlib.md5(password.encode()).hexdigest(),
		'xdvfb': yzm
	})

	req = request.Request(login_url, data=post_data.encode("gbk"), headers=headers)
	resp = opener.open(req)


def get_login_opener(id, password):
	opener = get_opener()
	login(opener, id, password)
	return opener


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


def is_login_success(t_data):
	"""
	判断登录是否成功
	:param t_data:
	:return:
	"""
	result = "学年学期状态" in t_data
	return result


if __name__ == '__main__':
	user_id = "2017302580196"
	password = "zl19990105"

	fail_count = 0
	while True:
		login_opener = get_login_opener(user_id, password)
		timetable_data = get_timetable(login_opener, 2019, 1)
		condition = is_login_success(timetable_data)

		if condition:
			print("登录成功！")
			break
		else:
			fail_count += 1
			print(f"登录第{fail_count}次失败，重新识别验证码并登录中......")

	ranges = get_courses_range(timetable_data)
	courses = get_course_list(ranges)
	display_timetable_data(courses)
