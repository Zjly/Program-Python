# 导入相关包
import numpy as np
import pandas as pd
from pandas import plotting

import matplotlib.pyplot as plt

plt.style.use('seaborn')

import seaborn as sns

sns.set_style("whitegrid")

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

# ——————————————————————————————————————————————————————0 准备数据———————————————————————————————————————————————————————
iris = pd.read_csv('iris.csv', usecols=[0, 1, 2, 3, 4])
# 设置颜色主题
antV = ['#1890FF', '#2FC25B', '#FACC14', '#223273', '#8543E0', '#13C2C2', '#3436c7', '#F04864']

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# # 数据显示
# iris.info()
# print(iris.head())

# ———————————————————————————————————————————1 探索性分析————————————————————————————————————————————————————————————————
# print(iris.describe())

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————


# # 绘制  Violinplot
# f, axes = plt.subplots(2, 2, figsize=(8, 8), sharex=True)
# sns.despine(left=True)
#
# # sns.violinplot(x轴数据, y轴数据, 数据来源, 颜色, 子区域)
# # violinplot与boxplot扮演类似的角色，它显示了定量数据在一个（或多个）分类变量的多个层次上的分布，这些分布可以进行比较。
# sns.violinplot(x='Species', y='SepalLengthCm', data=iris, palette=antV, ax=axes[0, 0])
# sns.violinplot(x='Species', y='SepalWidthCm', data=iris, palette=antV, ax=axes[0, 1])
# sns.violinplot(x='Species', y='PetalLengthCm', data=iris, palette=antV, ax=axes[1, 0])
# sns.violinplot(x='Species', y='PetalWidthCm', data=iris, palette=antV, ax=axes[1, 1])
#
# plt.show()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# # 绘制  pointplot
# f, axes = plt.subplots(2, 2, figsize=(8, 8), sharex=True)
# sns.despine(left=True)
#
# # sns.pointplot(x轴数据, y轴数据, 数据来源, 颜色, 子区域)
# # 点图代表散点图位置的数值变量的中心趋势估计，并使用误差线提供关于该估计的不确定性的一些指示。
# sns.pointplot(x='Species', y='SepalLengthCm', data=iris, color=antV[0], ax=axes[0, 0])
# sns.pointplot(x='Species', y='SepalWidthCm', data=iris, color=antV[0], ax=axes[0, 1])
# sns.pointplot(x='Species', y='PetalLengthCm', data=iris, color=antV[0], ax=axes[1, 0])
# sns.pointplot(x='Species', y='PetalWidthCm', data=iris, color=antV[0], ax=axes[1, 1])
#
# plt.show()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# # 生成各特征之间关系的矩阵图
# g = sns.pairplot(data=iris, palette=antV, hue= 'Species')
# plt.show()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#  使用 Andrews Curves 将每个多变量观测值转换为曲线并表示傅立叶级数的系数，这对于检测时间序列数据中的异常值很有用。
# plt.subplots(figsize = (10,8))
# plotting.andrews_curves(iris, 'Species', colormap='cool')
#
# plt.show()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 下面分别基于花萼和花瓣做线性回归的可视化：
# g = sns.lmplot(data=iris, x='SepalWidthCm', y='SepalLengthCm', palette=antV, hue='Species')
# g = sns.lmplot(data=iris, x='PetalWidthCm', y='PetalLengthCm', palette=antV, hue='Species')
# plt.show()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 通过热图找出数据集中不同特征之间的相关性，高正值或负值表明特征具有高度相关性：
# 从热图可看出，花萼的宽度和长度不相关，而花瓣的宽度和长度则高度相关。
# fig=plt.gcf()
# fig.set_size_inches(12, 8)
# fig=sns.heatmap(iris.corr(), annot=True, cmap='GnBu', linewidths=1, linecolor='k', square=True, mask=False, vmin=-1, vmax=1, cbar_kws={"orientation": "vertical"}, cbar=True)
# plt.show()

# —————————————————————————————————————————2 机器学习————————————————————————————————————————————————————————————————————
# 载入特征和标签集
# X = iris[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
# y = iris['Species']
#
# # 对标签集进行编码
# encoder = LabelEncoder()
# y = encoder.fit_transform(y)
# print(y)

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 将数据集以 7: 3 的比例，拆分为训练数据和测试数据
# train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3)
# # print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)
#
# import warnings
#
# warnings.filterwarnings("ignore")

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 检查不同模型的准确性
# Support Vector Machine 支持向量机
# model = svm.SVC()
# model.fit(train_X, train_y)
# prediction = model.predict(test_X)
# print('The accuracy of the SVM is: {0}'.format(metrics.accuracy_score(prediction, test_y)))

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# # Logistic Regression 逻辑回归
# model = LogisticRegression()
# model.fit(train_X, train_y)
# print(model)
#
# prediction = model.predict(test_X)
# print('预测的结果',prediction)
# print('实际的结果',test_y)
# print('The accuracy of the Logistic Regression is: {0}'.format(metrics.accuracy_score(prediction, test_y)))

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# # Decision Tree 决策树
# model = DecisionTreeClassifier()
# model.fit(train_X, train_y)
# prediction = model.predict(test_X)
# print('The accuracy of the Decision Tree is: {0}'.format(metrics.accuracy_score(prediction, test_y)))

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# # K-Nearest Neighbours  K最近邻分类算法
# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(train_X, train_y)
# prediction = model.predict(test_X)
# print('The accuracy of the KNN is: {0}'.format(metrics.accuracy_score(prediction, test_y)))

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 上面使用了数据集的所有特征，下面将分别使用花瓣和花萼的尺寸：
# petal = iris[['PetalLengthCm', 'PetalWidthCm', 'Species']]
# train_p,test_p=train_test_split(petal,test_size=0.3,random_state=0)
# train_x_p=train_p[['PetalWidthCm','PetalLengthCm']]
# train_y_p=train_p.Species
# test_x_p=test_p[['PetalWidthCm','PetalLengthCm']]
# test_y_p=test_p.Species
#
# sepal = iris[['SepalLengthCm', 'SepalWidthCm', 'Species']]
# train_s,test_s=train_test_split(sepal,test_size=0.3,random_state=0)
# train_x_s=train_s[['SepalWidthCm','SepalLengthCm']]
# train_y_s=train_s.Species
# test_x_s=test_s[['SepalWidthCm','SepalLengthCm']]
# test_y_s=test_s.Species
#
# model=svm.SVC()
#
# model.fit(train_x_p,train_y_p)
# prediction=model.predict(test_x_p)
# print('The accuracy of the SVM using Petals is: {0}'.format(metrics.accuracy_score(prediction,test_y_p)))
#
# model.fit(train_x_s,train_y_s)
# prediction=model.predict(test_x_s)
# print('The accuracy of the SVM using Sepal is: {0}'.format(metrics.accuracy_score(prediction,test_y_s)))