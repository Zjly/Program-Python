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

comments = comments.values

comments1 = comments[0:1000, :]
comments2 = comments[1000:2000, :]
comments3 = comments[2000:3000, :]
comments4 = comments[3000:, :]

comments1 = pd.DataFrame(comments1)
comments2 = pd.DataFrame(comments2)
comments3 = pd.DataFrame(comments3)
comments4 = pd.DataFrame(comments4)

# comments1.to_csv("comments1.csv", sep=",", index=None, encoding="utf-8")
# comments2.to_csv("comments2.csv", sep=",", index=None, encoding="utf-8")
# comments3.to_csv("comments3.csv", sep=",", index=None, encoding="utf-8")
# comments4.to_csv("comments4.csv", sep=",", index=None, encoding="utf-8")