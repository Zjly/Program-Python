import IPython as IPython
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# # ————————————————————Series——————————————————————

# # 使用列表
# s1 = pd.Series([1212, 2, 3, 4])
#
# # 使用可迭代对象
# s2 = pd.Series(range(10))
#
# # 使用nparray数组
# s3 = pd.Series(np.array([1, 2, 3, 4]))
#
# # 使用字典
# #s4 = pd.Series(["a":"xy", "b":"34234", "c":"3243"])
#
# # 标量
# s5 = pd.Series(33)
#
# s6 = pd.Series(33, index=["k", "x", "y"])
#
# print(s1)
# print(s2)
# print(s3)
# #print(s4)
# print(s5)
# print(s6)

# ——————————————————————————————————————————

# s = pd.Series([1, 2, 3])
# s2 = pd.Series([4, 5, 6])
#
# # 矢量运算
# print(s * s2)
#
# # 标量运算
# print(s * 5)
#
# # 对于numpy的一些函数，也可以使用
# print(np.mean(s))

# s = pd.Series([1, 2, 3], index=[1, 2, 3])
# s2 = pd.Series([4, 5, 6], index=[2, 3, 4])
# print(s)
# print(s2)
#
# # 索引值不同 理解为外键对不上 产生NAN
# print(s + s2)
#
# print(s.add(s2, fill_value=100))
#
# # 是否是空
# print(s.isnull)

# a = np.array([1, 2, 3, 4, np.nan])
# b = pd.Series([1, 2, 3, 4, np.nan])
# print(np.mean(a))
# print(np.mean(b))

# ——————————————————————————————————————————

# # 索引 loc标签索引访问 iloc位置索引访问
# s = pd.Series([1, 2, 3], index=list("abc"))
# print(s.loc["b"])
# print(s.iloc[0])

# ——————————————————————————————————————————

# # 切片
# s = pd.Series([1, 2, 3, 4], index=list("abcd"))
#
# print(s.iloc[0:3])
# print(s.loc["a":"d"])

# ——————————————————————————————————————————

# s = pd.Series([1, 2, 3, 4], index=list("abcd"))
# print(s.loc["a"])
#
# # 修改值
# s.loc["a"] = 3000
# print(s)
#
# # 增加值
# s.loc["new_key"] = "1615165651"
# print(s)
#
# # 删除值 类似字典
# del s["a"]
# print(s)
#
# # 删除值 通过drop方法 inplace就地修改
# print(s.drop("d", inplace=True))
#
# # 删除多个值
# print(s.drop(["b", "new_key"], inplace=False))

# ——————————————————————————————————————————

# # DataFrame创建方式
# df1 = pd.DataFrame(np.random.rand(3, 5))
# df2 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
# print(df1)
# print(df2)
#
# # 显示前后几条记录
# print(df2.head(2))
# print(df2.tail(2))

# ——————————————————————————————————————————

# df = pd.DataFrame(np.random.rand(3, 5),
# 				  index=["地区1", "地区2", "地区3"],
# 				  columns=["北京", "天津", "上海", "广州", "沈阳"])
# print(df)
#
# # 行索引
# print(df.index)
#
# # 列索引
# print(df.columns)
#
# # 值
# print(df.values)
#
# # 大小
# print(df.shape)
#
# # 维度
# print(df.ndim)
#
# # 类型
# print(df.dtypes)

# ——————————————————————————————————————————

# # 排序
# df = pd.DataFrame([[1, 4], [3, 2]], index=[2, 1], columns=list("ab"))
# print(df)
# print(df.sort_values("b"))

# ——————————————————————————————————————————

# 统计函数

# df = pd.DataFrame(np.random.rand(5, 5),
# 				  columns=list("abcde"),
# 				  index=list("hijkl"))
# print(df)
# print(df.info())
# print(df.describe())

# ———————————————————matplotlib———————————————————————

# # 2D图
#
# #解决qt中文乱码
# plt.rcParams["font.family"] = "SimHei"
# plt.rcParams["axes.unicode_minus"] = False
#
# x = np.linspace(-10, 10, 200)
# # print(x,type(x),x.shape)
#
# y1 = 2 * x + 10
# y2 = x ** 2
#
# # 创建画布
# plt.figure()
# #绘制直线
# plt.plot(x, y1,"g-",label="直线")
# #绘制抛物线
# plt.plot(x, y2, "r-", linewidth = 1.0, linestyle = '--',label="抛物线")
#
# plt.xlabel('x轴')
# plt.ylabel('y轴')
# plt.legend()
# plt.show()

# ——————————————————————————————————————————

# # 定义figure
# fig = plt.figure()
# # 将figure变为3d
# ax = Axes3D(fig)
#
# # 定义x, y
# x = np.arange(-4, 4, 0.2)
# y = np.arange(-4, 4, 0.2)
#
# # 生成网格数据
# X, Y = np.meshgrid(x, y)
#
# # 计算每个点对的长度
# R = np.sqrt(X ** 2 + Y ** 2)
# # 计算Z轴的高度
# Z = np.sin(R)
#
# # 绘制3D曲面
# ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = 'rainbow',alpha=0.8)
# # 绘制从3D曲面到底部的投影
# # ax.contour(X, Y, Z, zdir = 'z', offset = -2, cmap = 'rainbow')
# # 设置z轴的维度
# ax.set_zlim(-2, 2)
#
# plt.show()

# ——————————————————————————————————————————

# fig = plt.figure()
# ax = Axes3D(fig)
#
# x = np.random.randint(0, 500, 100)
# y = np.random.randint(0, 500, 100)
# z = np.random.randint(-200, 200, 100)
# y3 = np.arctan2(x, y)
# ax.scatter(x, y, z, c=y3, marker='.', s=1500)
# plt.show()
