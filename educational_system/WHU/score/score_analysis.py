import re


def read_pages():
	"""
	从html文件中读取网页源代码
	:return:
	"""
	with open("./score.html", "r") as fp:
		html = fp.read()
		return html


def get_score_range(data):
	"""
	得到包含有分数的范围的网页源代码
	:param data: 网页源代码
	:return: 分隔为每一门课的，包含有成绩信息的网页源代码list
	"""
	pattern = "<tr null>(.*?)</tr>"
	p = re.compile(pattern, re.S)
	scores_range = p.findall(data)
	return scores_range


def get_course_list(score_range):
	"""
	得到课程成绩信息list
	:param score_range: 包含有课程成绩信息的网页源代码
	:return: 课程成绩信息list
	"""
	course_list = []
	for course_score in score_range:
		# 匹配出每一个信息元素
		pattern = "<td>(.*?)</td>"
		p = re.compile(pattern, re.S)
		course_data = p.findall(course_score)
		for i in range(len(course_data)):
			course_data[i] = course_data[i].replace("\t", "").replace("\n", "").replace(" ", "")

		course_id = course_data[0]
		course_name = course_data[1]
		course_type = course_data[2][course_data[2].index(">") + 1:course_data[2].index(">") + 5]
		course_credit = course_data[5]
		course_teacher = course_data[6]
		course_year = course_data[9]
		course_semester = course_data[10]
		course_score = course_data[11]
		course = [course_id, course_name, course_type, course_credit, course_teacher, course_year, course_semester,
				  course_score]
		course_list.append(course)

	return course_list


def display_course_list(course_list):
	"""
	显示课程信息
	:param course_list:
	:return:
	"""
	for course in course_list:
		print(course)


def calculate_GPA(course_list):
	"""
	计算GPA并显示
	:param course_list: 课程信息list
	:return:
	"""
	sum_credit = 0
	sum_GPA = 0
	for course in course_list:
		if course[7] != "":
			course_score = float(course[7])
			course_credit = float(course[3])
			course_GPA = get_GPA_from_score(course_score)
			sum_GPA += course_GPA * course_credit
			sum_credit += course_credit
	print("全部GPA:" + str(sum_GPA / sum_credit))

	sum_credit = 0
	sum_GPA = 0
	for course in course_list:
		if course[7] != "" and (course[2].find("选修") == -1):
			course_score = float(course[7])
			course_credit = float(course[3])
			course_GPA = get_GPA_from_score(course_score)
			sum_GPA += course_GPA * course_credit
			sum_credit += course_credit
	print("保研GPA:" + str(sum_GPA / sum_credit))

def get_GPA_from_score(score):
	score = float(score)
	"""
	根据分数返回对应的GPA
	:param score: 该课程分数
	:return: 该课程GPA
	"""
	if score >= 90:
		return 4.0
	elif score >= 85:
		return 3.7
	elif score >= 82:
		return 3.3
	elif score >= 78:
		return 3.0
	elif score >= 75:
		return 2.7
	elif score >= 72:
		return 2.3
	elif score >= 68:
		return 2.0
	elif score >= 64:
		return 1.5
	elif score >= 60:
		return 1.0
	else:
		return 0.0

def main():
	score_page = read_pages()
	ranges = get_score_range(score_page)
	course_score_list = get_course_list(ranges)
	display_course_list(course_score_list)
	calculate_GPA(course_score_list)

if __name__ == '__main__':
	main()