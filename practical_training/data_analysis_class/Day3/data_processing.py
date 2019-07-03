import numpy as np
import pandas as pd
import sqlite3
import pymysql
from IPython.core.display import display

# read_csv read_table
# 可以读很多的文本文件

# 链接数据库
# conn = sqlite3.connect("test.db")
#
# conn.execute("create table of not exists person (id int primary key, name varchar(30), age int)")
#
# conn.execute("insert into person(id, name, age) values(38, 'aaa', 17)")
#
# t = pd.read_sql("select id, name, age from person", conn)
# print(t)
# conn.close()

# ——————————————————————————————————————————

# conn = pymysql.connect("localhost", "root", "root", "class")
# t = pd.read_sql(sql="select * from cm_course", con=conn)
# display(t)

# ——————————————————————————————————————————

# # 数据写入
# df = pd.DataFrame(np.arange(15).reshape(3, 5))
# df[5] = np.nan
# print(df)
#
# # sep自定义分隔符
# df.to_csv("wf.txt", sep="-")
#
# # 不保存索引
# df.to_csv("wf.txt", header=False, sep="&")
# df.to_csv("wf.txt", header=False, index=False, sep=",")
#
# # 空值设置
# df.to_csv("wf.txt", header=False, index=False, na_rep="空")

# ————————————————————数据清洗——————————————————————

# # 缺失值处理
# df = pd.DataFrame(np.arange(15).reshape(3, 5))
# df[5] = np.nan
# # display(df)
# #
# # df.info()
# # display(df.isnull())
#
# # 删除空值 thresh:非空数值达到阈值就保留 否则删除
# # df = df.dropna()
#
# # 填充空值 fillna    ffill 上方    bfill 下方
# df = df.fillna(10)
# #
# # df = df.fillna({5: 0})
# #
# print(df)
#
# print(df[[0, 1, 2, 3, 4, 5]].describe())

# ——————————————————————————————————————————

# conn = pymysql.connect("localhost", "root", "root", "class")
# df = pd.read_sql(sql="select * from cm_course", con=conn)
#
# # 查看重复值
# # print(df.duplicated())
#
# # 查看重复记录
# # print(df[df.duplicated()])
#
# # 删除重复值
# # df.drop_duplicates()
#
# conn.close()

# ——————————————————————————————————————————

# # 数据过滤
# conn = pymysql.connect("localhost", "root", "root", "class")
# df = pd.read_sql(sql="select * from cm_course", con=conn)
#
# # 查询1
# # display(df[df["course_college"] == "计算机学院"])
#
# # 查询2
# s = "文学院"
# display(df.query("course_college == @s"))
#
#
# conn.close()

# ——————————————————————————————————————————

# apply定义函数处理逻辑

# conn = pymysql.connect("localhost", "root", "root", "class")
# df = pd.read_sql(sql="select * from cm_course", con=conn)
# conn.close()

# # 显示前5行
# print(df.head())
#
# # 采样
# print(df.sample(2))

# 替换
# s = df["course_college"]
# print(s)
# print(s.replace(["文学院", "电子信息学院"], ["wx院", "dx院"]))
# print(s.replace({"文学院": "wx院", "电子信息学院": "dx院"}))

# ——————————————————————————————————————————

# conn = pymysql.connect("localhost", "root", "root", "class")
# df = pd.read_sql(sql="select * from cm_course", con=conn)
# conn.close()

# 数据合并
# head = df.head()
# tail = df.tail()
#
# print(pd.concat((head, tail)))

# ——————————————————————————————————————————


# 读取csv文件，返回一个DataFrame类型的对象。
# 在读取的时候，默认会将第一行记录当成标题。
# 如果没有标题，我们可以指定header=None。
# 如果header为None，read_csv默认会自己生成列标签。（0， 1， 2， 3……）。
# df = pd.read_csv("./data/iris.csv", header=None,skiprows=1)

# read_csv默认使用逗号作为分隔符，我们可以使用sep或delimiter来指定分隔符。
# df = pd.read_csv("./data/1.txt", sep="\t")
# df = pd.read_table("./data/1.txt",header=None)

# 我们可以通过names参数来指定列标签（标题）
# df = pd.read_table("./data/1.txt",header=None,names=["姓名", "科目", "分数"])

# 如果我们需要自己指定某列充当行索引（例如，数据库，数据表中的主键）
# 可以使用index_col参数来进行设置。
# df = pd.read_table("./data/1.txt",header=None, index_col=0)

# 我们可以使用usecols来控制需要哪些列。如果某列充当索引列（index_col），
# 则充当索引列的标签，也需要指定在usecols中。

# df = pd.read_table("./data/1.txt", header=None, index_col=0, usecols=[0, 2])

# print(df)
# display(df)