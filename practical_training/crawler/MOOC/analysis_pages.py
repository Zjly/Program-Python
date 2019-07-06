import os
import re


def read_html_pages():
	root_path = 'E:\Coding\Python\Program\practical_training\crawler\MOOC\course_data'
	page_list = os.listdir(root_path)  # 列出文件夹下所有的目录与文件
	course_data_list = []
	for i in range(0, len(page_list)):
		path = os.path.join(root_path, page_list[i])
		if os.path.isfile(path):
			with open(path, "r", encoding="utf-8") as fp:
				page = fp.read()
				course_data_list.append(analysis_html(path, page))

	print()


def analysis_html(path, page):
	# 匹配老师id
	pattern = "memberId\s*:\s*\"(.*?)\","
	p = re.compile(pattern, re.S)
	teacher_id = p.findall(page)

	# 匹配老师名字
	pattern = "lectorName\s*:\s*\"(.*?)\","
	p = re.compile(pattern, re.S)
	teacher_name = p.findall(page)

	# 匹配课程名称
	pattern = "window.courseDto = {\nname\s*:\s*\"(.*?)\","
	p = re.compile(pattern, re.S)
	course_name = p.findall(page)

	# 匹配课程id
	course_id = path.replace("E:\Coding\Python\Program\practical_training\crawler\MOOC\course_data\\", "").replace(
		".html", "")

	# 匹配课程类型
	pattern = "window.categories = (.*?);"
	p = re.compile(pattern, re.S)
	course_type_range = p.findall(page)

	pattern = "name\s*:\s*\"(.*?)\",\ntype"
	p = re.compile(pattern, re.S)
	course_type = p.findall(course_type_range[0])

	# 匹配课程学校
	pattern = "window.schoolDto = (.*?);"
	p = re.compile(pattern, re.S)
	course_school_range = p.findall(page)

	pattern = "name\s*:\s*\"(.*?)\",\nbigLogo"
	p = re.compile(pattern, re.S)
	course_school = p.findall(course_school_range[0])

	# 匹配课程介绍
	pattern = "spContent=(.*?),中国大学MOOC（慕课）"
	p = re.compile(pattern, re.S)
	course_introduce = p.findall(page)

	course_data = [teacher_id[0], teacher_name[0], course_name[0], course_id, course_type[len(course_type) - 1],
				   course_school[0], course_introduce[0]]
	return course_data


if __name__ == '__main__':
	read_html_pages()
