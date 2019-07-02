import numpy as np

# ————————————————————ndarray n维数组——————————————————————
# li = [1., 28, 10]
#
# nd = np.array(li)
#
# print(type(nd))
# print(nd.dtype)

# ——————————————————————————————————————————

# 元素数据类型一致，矢量化运算
# nd7 = np.random.randint(1, 100, (5, 6))

# # 通过索引
# print(nd7)
#
# # 访问列表的方式
# print(nd7[0])
# print(nd7[0][2])
#
# # 访问矩阵的方式 下标索引[2][1]
# print(nd7[2, 1])
#
# # 通过整数数组 行索引 第[1][3]行
# print(nd7[[1, 3]])
#
# # 通过布尔数组
# print(nd7[[True, False, True, False, True]])

# ——————————————————————————————————————————

# #切片
# print(nd7)
#
# # 从0行到2行 不包括第二行
# print(nd7[0:2])
#
# # 从0行到2行 不包括第二行，再从里面取所有列
# print(nd7[0:2,:])
#
# # 取第一行
# print(nd7[1,:])
#
# # 取第二列
# print(nd7[:,2])
#
# # 取到倒数第一列
# print(nd7[:,:-1])

# ——————————————————————————————————————————

# # ndarray扁平化操作
# x = np.arange(12).reshape(3, 2, 2)
# print(x)
# print("***" * 10)
#
# # # 扁平化操作 返回视图 会改变
# # y = np.ravel(x)
# # y[0] = 1000
# # print(x, y)
#
# # 扁平化操作 返回拷贝 不会改变
# y = x.flatten()
# y[0] = 1000
# print(x, y)

# ——————————————————————————————————————————

# 统计函数 sum 等

# ————————————————————matrix 矩阵——————————————————————

# a = np.mat([1, 2, 3])
# print(a, type(a))
#
# # 通过ndarray转换
# c = np.array([4, 5, 6])
# b = np.mat(c)
# print(b, type(b))
# print(b.shape)
#
# # 矩阵转置
# print(a * b.T)
# print(a.T * b)
#
# # 广播 对应的位置相乘
# print(np.multiply(a, b.T))

# ——————————————————————————————————————————