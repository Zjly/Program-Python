import pandas as pd
import pymysql


def get_comment_from_database():
	"""
	从数据库中得到评论
	:return: 评论的DataFramework
	"""
	conn = pymysql.connect("localhost", "root", "root", "test")
	return pd.read_sql(sql="select comment_content, comment_quality from cm_comment", con=conn)


if __name__ == '__main__':
	comments = get_comment_from_database()
