import pandas as pd
import pymysql

db = pymysql.connect("localhost", "root", "root", "test")
cursor = db.cursor()


def get_course_number():
	course_id_list = pd.read_sql(sql="select course_id from cm_course", con=db)
	print(course_id_list)


if __name__ == '__main__':
	get_course_number()
