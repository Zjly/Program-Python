import pandas as pd
import pymysql

conn = pymysql.connect("localhost", "root", "root", "test")
comments = pd.read_sql(sql="select comment_content, comment_quality from cm_comment", con=conn)
comments.columns = ["comment", "evaluation"]

comments = comments.replace("\n", "", regex=True)
comments = comments.replace(",", "，", regex=True)
comments = comments.replace(" ", "，", regex=True)
comments = comments.replace("\t", "，", regex=True)
comments = comments.replace("medium", "good", regex=True)
# comments = comments.replace("good", "1")
# comments = comments.replace("bad", "0")

comments.to_csv("comments.csv", sep=",", index=None)
