import numpy as np
import pandas as pd
from IPython.core.display import display

# 读取csv文件，返回一个DataFrame类型的对象。
# 在读取的时候，默认会将第一行记录当成标题。
# 如果没有标题，我们可以指定header=None。
# 如果header为None，read_csv默认会自己生成列标签。（0， 1， 2， 3……）。
df = pd.read_csv("./data/iris.csv", header=None,skiprows=1)

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
display(df)