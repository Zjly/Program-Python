import pandas as pd

from practical_training.machine_learning.course_recommendation.read_data import read_data_from_database


def create_inverted_matrix(selects, students, courses):
	"""
	创建学生与课程的倒排矩阵
	:param selects: 选课记录
	:param students: 学生表
	:param courses: 课程表
	:return: 倒排矩阵
	"""
	s = students["student_number"].values.tolist()
	c = courses["cID"].values.tolist()
	df = pd.DataFrame(index=s, columns=c)
	df = df.fillna(0)

	# 将选课信息填入矩阵中
	for row in selects.iterrows():
		df.loc[row[1]["student_number"], row[1]["cID"]] = 1
	return df


def create_co_occurrence_matrix(matrix, courses):
	"""
	构建物品与物品的同现矩阵，共现矩阵C表示同时喜欢两个物品的用户数，是根据用户物品倒排表计算出来的
	:param matrix: 倒排矩阵
	:param courses: 课程表
	:return: 同现矩阵
	"""
	c = courses["cID"].values.tolist()
	df = pd.DataFrame(index=c, columns=c)
	df = df.fillna(0)

	for row in matrix.index:
		for column1 in matrix.columns:
			# 遍历每一个元素，找出矩阵内为1的元素
			if matrix.loc[row, column1] == 1:
				# 若该元素为1，遍历同行内所有元素，若有为1的将这两元素加入同现矩阵
				for column2 in matrix.columns:
					if matrix.loc[row, column2] == 1 and column1 != column2:
						df.loc[column1, column2] = df.loc[column1, column2] + 1

	return df


def create_num_matrix(matrix, courses):
	"""
	创建选课人数矩阵
	:param matrix: 倒排矩阵
	:param courses: 课程表
	:return: 选课人数矩阵
	"""
	c = courses["cID"].values.tolist()
	df = pd.DataFrame(index=["num"], columns=c)
	df = df.fillna(0)

	for row in matrix.index:
		for column in matrix.columns:
			if matrix.loc[row, column] == 1:
				df.loc["num", column] = df.loc["num", column] + 1

	return df


def create_similarity_matrix(c_matrix, n_matrix, courses):
	"""
	创建相似矩阵
	:param c_matrix: 同现矩阵
	:param n_matrix: 人数矩阵
	:param courses: 选课表
	:return: 相似矩阵
	"""
	c = courses["cID"].values.tolist()
	df = pd.DataFrame(index=c, columns=c)
	df = df.fillna(0)

	for row in c_matrix.index:
		for column in c_matrix.columns:
			if n_matrix.loc["num", column] != 0:
				df.loc[row, column] = c_matrix.loc[row, column] / (
						(n_matrix.loc["num", row] * n_matrix.loc["num", column]) ** 0.5)

	return df


def create_recommendation_matrix(i_matrix, s_matrix, students, courses):
	"""
	创建推荐矩阵
	:param i_matrix: 倒排矩阵
	:param s_matrix: 相似矩阵
	:param students: 学生表
	:param courses: 选课表
	:return:
	"""
	s = students["student_number"].values.tolist()
	c = courses["cID"].values.tolist()
	df = pd.DataFrame(index=s, columns=c)
	df = df.fillna(0)

	# 遍历倒排矩阵中的每一个0元素（用户未选该课程）
	for row in i_matrix.index:
		for column1 in i_matrix.columns:
			if i_matrix.loc[row, column1] == 0:
				interest = 0
				# 计算兴趣度
				for column2 in i_matrix.columns:
					interest = interest + i_matrix.loc[row, column2] * s_matrix.loc[column1, column2]
				df.loc[row, column1] = interest

	return df

def get_recommended_courses(student, r_matrix, count):
	"""
	得到推荐课程的课程号
	:param student: 想要推荐课程的学生号
	:param r_matrix: 推荐矩阵
	:param count: 推荐课程数
	:return: 推荐课程课程号list
	"""
	recommended = r_matrix.loc[student,:]
	recommended_sort = recommended.sort_values(ascending=False)
	recommended_course_list = []
	for i in range(count):
		recommended_course_list.append(recommended_sort.index[i])
	return recommended_course_list

if __name__ == '__main__':
	selection_list, student_list, course_list = read_data_from_database()
	inverted_matrix = create_inverted_matrix(selection_list, student_list, course_list)
	co_occurrence_matrix = create_co_occurrence_matrix(inverted_matrix, course_list)
	num_matrix = create_num_matrix(inverted_matrix, course_list)
	similarity_matrix = create_similarity_matrix(co_occurrence_matrix, num_matrix, course_list)
	recommendation_matrix = create_recommendation_matrix(inverted_matrix, similarity_matrix, student_list, course_list)
	recommended_courses = get_recommended_courses("31231", recommendation_matrix, 3)
