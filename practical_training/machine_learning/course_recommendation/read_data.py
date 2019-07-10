import pymysql
import pandas as pd


def read_data_from_database():
	"""
	从数据库中读取选课信息
	:return: 选课信息DataFrame
	"""
	db = pymysql.connect("localhost", "root", "root", "test")
	# db = pymysql.connect(host="cdb-5oviul9n.gz.tencentcdb.com", port=10094, user="root", passwd="Ab123123",
	# 					 db="class_manage")
	sql_get_course_selection = "SELECT student_number, cID FROM CM_student_course"
	select_data = pd.read_sql(sql=sql_get_course_selection, con=db)

	sql_get_student = "SELECT distinct student_number FROM CM_student_course"
	student_data = pd.read_sql(sql=sql_get_student, con=db)

	sql_get_course = "SELECT distinct cID FROM CM_student_course"
	course_data = pd.read_sql(sql=sql_get_course, con=db)

	db.close()
	return select_data, student_data, course_data
