import re
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def crawler():
	chrome_driver = "C:\Program Files (x86)\Google\Chrome\chromedriver.exe"
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)

	url = "http://www.icourse163.org/category/all"
	driver.get(url)

	course_url_list = []
	for i in range(2):
		page_html = driver.page_source
		course_url_list = course_url_list + get_course_url_from_page(page_html)

		next_button = driver.find_element_by_link_text("下一页")
		driver.execute_script("arguments[0].click();", next_button)

	course_data_list = []
	teacher_data_list = []
	for course_url in course_url_list:
		driver.get(course_url)
		course_data_html = driver.page_source
		course_data = get_course_data(course_url, course_data_html)
		course_data_list.append(course_data)

	# teacher_button = driver.find_element_by_link_text(course_data[1])
	# driver.execute_script("arguments[0].click();", teacher_button)
	# teacher_html = driver.page_source

	driver.close()
	driver.quit()


def get_course_url_from_page(page_html):
	"""
	得到该页面中所有课程信息
	:param page_html: 页面html的源代码
	:return: 该页面中所有课程的链接list
	"""
	# 找到包含有课程链接的区域
	pattern = "<!--Regular if35-->(.*?)<!--Regular if43-->"
	p = re.compile(pattern, re.S)
	url_range = p.findall(page_html)

	# 对该区域内内容进行课程链接的匹配
	pattern = "<a href=\"//(.*?)\" target=\"_blank\">"
	p = re.compile(pattern, re.S)
	urls = p.findall(url_range[0])
	final_data = list(set(urls))
	return final_data


def get_course_data(course_url, course_data_html):
	"""
	根据网页源码读取课程信息
	:param course_url: 课程链接
	:param course_data_html: 课程网页源代码
	:return: 课程信息List
	"""
	# 匹配老师id
	pattern = "memberId\s*:\s*\"(.*?)\","
	p = re.compile(pattern, re.S)
	teacher_id = p.findall(course_data_html)

	# 匹配老师名字
	pattern = "lectorName\s*:\s*\"(.*?)\","
	p = re.compile(pattern, re.S)
	teacher_name = p.findall(course_data_html)

	# 匹配课程名称
	pattern = "window.courseDto = {\nname\s*:\s*\"(.*?)\","
	p = re.compile(pattern, re.S)
	course_name = p.findall(course_data_html)

	# 匹配课程id
	course_id = course_url.replace("www.icourse163.org/course/", "")

	# 匹配课程类型
	pattern = "window.categories = (.*?);"
	p = re.compile(pattern, re.S)
	course_type_range = p.findall(course_data_html)

	pattern = "name\s*:\s*\"(.*?)\",\ntype"
	p = re.compile(pattern, re.S)
	course_type = p.findall(course_type_range[0])

	# 匹配课程学校
	pattern = "window.schoolDto = (.*?);"
	p = re.compile(pattern, re.S)
	course_school_range = p.findall(course_data_html)

	pattern = "name\s*:\s*\"(.*?)\",\nbigLogo"
	p = re.compile(pattern, re.S)
	course_school = p.findall(course_school_range[0])

	# 匹配课程介绍
	pattern = "spContent=(.*?),中国大学MOOC（慕课）\">"
	p = re.compile(pattern, re.S)
	course_introduce = p.findall(course_data_html)

	course_data = [teacher_id[0], teacher_name[0], course_name[0], course_id, course_type[len(course_type) - 1],
				   course_school[0], course_introduce[0]]
	return course_data


if __name__ == '__main__':
	crawler()
