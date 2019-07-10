import pandas as pd
import pymysql


def test():
	comments_data = pd.read_csv("./comments/comments.csv")

	db = pymysql.connect("localhost", "root", "root", "test")
	cursor = db.cursor()

	for i in range(len(comments_data)):
		a = comments_data.loc[i, "comment"]
		b = comments_data.loc[i, "evaluation"]
		sql = "INSERT INTO test VALUES ('%s', '%s')" % (a, b)
		cursor.execute(sql)


	try:
		db.commit()
	except:
		db.rollback()


if __name__ == '__main__':
	test()
