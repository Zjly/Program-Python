import pandas as pd
import pymysql


def read_comments_from_csv():
	"""
	从csv文件中读取评论信息
	:return:评论list
	"""
	comments = pd.read_csv("comments.csv", sep="|", header=None)
	return comments


def write_comment_database(comments):
	"""
	将评论写入数据库
	:param comments: 评论列表
	:return:
	"""
	db = pymysql.connect("localhost", "root", "root", "test")
	# db = pymysql.connect(host="cdb-5oviul9n.gz.tencentcdb.com", port=10094, user="root", passwd="Ab123123",
	# 					 db="class_manage")
	cursor = db.cursor()

	# 清空数据库内原有内容
	truncate_sql = "TRUNCATE TABLE CM_comment"
	cursor.execute(truncate_sql)

	for i in range(len(comments)):
		comment_connent = comments[3][i].replace("\'", "")
		comment_sql = "INSERT INTO CM_comment(course_id, student_name, comment_quality, comment_content, comment_time) VALUES ('%s', '%s', '%s', '%s', '%s')" % (
			comments[0][i], comments[1][i], comments[2][i], comment_connent, comments[4][i])
		cursor.execute(comment_sql)

	try:
		db.commit()
	except:
		db.rollback()


if __name__ == '__main__':
	comments = read_comments_from_csv()
	write_comment_database(comments)
