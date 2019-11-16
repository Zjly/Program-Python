import os

import numpy
import pandas
import sklearn
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import MultinomialNB, BernoulliNB, GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
import warnings
import cv2

from courses.business_intelligence.image_digitization import image_digitization, eigenvalue_extraction


def read_images(path):
	"""
	从文件中读取图像
	:return: 图像列表
	"""
	root_path = path
	file_list = os.listdir(root_path)  # 列出文件夹下所有的目录与文件
	image_list = []
	for i in range(0, len(file_list)):
		path = os.path.join(root_path, file_list[i])
		if os.path.isfile(path):
			name = "****"
			image = cv2.imread(path)
			image_list.append([name, image])

	return image_list


def read_data_from_csv():
	"""
	从csv文件中读取训练数据
	:return: 数据集，标签集
	"""
	data_list = pandas.read_csv("./data.csv", header=None)

	labels = data_list[0]
	characteristics = data_list.iloc[:, 1:]

	return characteristics, labels


def machine_learning(c_list, l_list):
	"""
	各类机器学习算法测试 https://www.jianshu.com/p/731610dca805
	:param c_list: 数据集
	:param l_list: 标签集
	:return:
	"""
	warnings.filterwarnings("ignore")

	train_X, test_X, train_y, test_y = train_test_split(c_list, l_list, test_size=0.3, random_state=42)

	# 线性回归
	# fit_intercept：是否计算截距。False-模型没有截距
	# normalize： 当fit_intercept设置为False时，该参数将被忽略；如果为真，则回归前的回归系数X将通过减去平均值并除以l2-范数而归一化。
	# copy_X：是否对X数组进行复制,默认为True
	# n_jobs：指定线程数
	# model = sklearn.linear_model.LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=4)
	# model.fit(train_X, train_y)
	# prediction = model.predict(test_X)
	# print('线性回归算法的准确率为: {0}'.format(sklearn.metrics.accuracy_score(prediction, test_y)))

	# 逻辑回归
	# penalty：使用指定正则化项（默认：l2）
	# dual: n_samples > n_features取False（默认）
	# C：正则化强度的反，值越小正则化强度越大
	# n_jobs: 指定线程数
	# fit_intercept: 是否需要常量
	model = sklearn.linear_model.LogisticRegression(penalty='l2', dual=False, C=1.0, n_jobs=4, fit_intercept=True)
	model.fit(train_X, train_y)
	prediction = model.predict(test_X)
	# print('逻辑回归算法的准确率为: {0}'.format(sklearn.metrics.accuracy_score(prediction, test_y)))
	score = cross_val_score(model, X=c_list, y=l_list, cv=10)
	print(f'逻辑回归算法的平均准确率为: {numpy.mean(score)}')

	# 朴素贝叶斯
	# alpha：平滑参数
	# fit_prior：是否要学习类的先验概率；false-使用统一的先验概率
	# class_prior: 是否指定类的先验概率；若指定则不能根据参数调整
	# binarize: 二值化的阈值，若为None，则假设输入由二进制向量组成

	# 多项式分布朴素贝叶斯
	# model = MultinomialNB(alpha=1.0, fit_prior=True, class_prior=None)
	# model.fit(train_X, train_y)
	# prediction = model.predict(test_X)
	# print('朴素贝叶斯算法(多项式分布)的准确率为: {0}'.format(sklearn.metrics.accuracy_score(prediction, test_y)))

	# 伯努利分布朴素贝叶斯
	model = BernoulliNB(alpha=1.0, binarize=0.0, fit_prior=True, class_prior=None)
	model.fit(train_X, train_y)
	prediction = model.predict(test_X)
	# print('朴素贝叶斯算法(伯努利分布)的准确率为: {0}'.format(sklearn.metrics.accuracy_score(prediction, test_y)))
	score = cross_val_score(model, X=c_list, y=l_list, cv=10)
	print(f'朴素贝叶斯算法(伯努利分布)的平均准确率为: {numpy.mean(score)}')

	# 高斯分布朴素贝叶斯
	model = GaussianNB()
	model.fit(train_X, train_y)
	prediction = model.predict(test_X)
	# print('朴素贝叶斯算法(高斯分布)的准确率为: {0}'.format(sklearn.metrics.accuracy_score(prediction, test_y)))
	score = cross_val_score(model, X=c_list, y=l_list, cv=10)
	print(f'朴素贝叶斯算法(高斯分布)的平均准确率为: {numpy.mean(score)}')

	# Decision Tree 决策树
	# criterion ：特征选择准则gini/entropy
	# max_depth：树的最大深度，None-尽量下分
	# min_samples_split：分裂内部节点，所需要的最小样本树
	# min_samples_leaf：叶子节点所需要的最小样本数
	# max_features: 寻找最优分割点时的最大特征数
	# max_leaf_nodes：优先增长到最大叶子节点数
	# min_impurity_decrease：如果这种分离导致杂质的减少大于或等于这个值，则节点将被拆分。
	model = DecisionTreeClassifier(criterion='entropy', max_depth=None, min_samples_split=2,
								   min_samples_leaf=1, max_features=None, max_leaf_nodes=None,
								   min_impurity_decrease=0)
	model.fit(train_X, train_y)
	prediction = model.predict(test_X)
	# print('决策树算法的准确率为: {0}'.format(metrics.accuracy_score(prediction, test_y)))
	score = cross_val_score(model, X=c_list, y=l_list, cv=10)
	print(f'决策树算法的平均准确率为: {numpy.mean(score)}')

	# 支持向量机
	# C：误差项的惩罚参数C
	# kernel：核函数选择 默认：rbf(高斯核函数)，可选：‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
	# gamma: 核相关系数。浮点数，If gamma is ‘auto’ then 1/n_features will be used instead.点将被拆分。
	model = SVC(C=1.0, kernel='rbf', gamma='auto')
	model.fit(train_X, train_y)
	prediction = model.predict(test_X)
	# print('支持向量机算法的准确率为: {0}'.format(sklearn.metrics.accuracy_score(prediction, test_y)))
	score = cross_val_score(model, X=c_list, y=l_list, cv=10)
	print(f'支持向量机算法的平均准确率为: {numpy.mean(score)}')

	# 神经网络
	# hidden_layer_sizes: 元祖
	# activation：激活函数 {‘identity’, ‘logistic’, ‘tanh’, ‘relu’}, 默认 ‘relu’
	# solver ：优化算法{‘lbfgs’, ‘sgd’, ‘Adam’}
	# alpha：L2惩罚(正则化项)参数
	# learning_rate：学习率 {‘constant’, ‘invscaling’, ‘adaptive’}
	# learning_rate_init：初始学习率，默认0.001
	# max_iter：最大迭代次数 默认200
	#
	# 特别：
	# 学习率中参数：
	# constant: 有‘learning_rate_init’给定的恒定学习率
	# incscaling：随着时间t使用’power_t’的逆标度指数不断降低学习率
	# adaptive：只要训练损耗在下降，就保持学习率为’learning_rate_init’不变
	# 优化算法参数：
	# lbfgs：quasi-Newton方法的优化器
	# sgd：随机梯度下降
	# adam： Kingma, Diederik, and Jimmy Ba提出的机遇随机梯度的优化器
	model = MLPClassifier(activation='tanh', solver='adam', alpha=0.0001,
						  learning_rate='adaptive', learning_rate_init=0.001, max_iter=1000)
	model.fit(train_X, train_y)
	prediction = model.predict(test_X)
	# print('神经网络算法的准确率为: {0}'.format(sklearn.metrics.accuracy_score(prediction, test_y)))
	score = cross_val_score(model, X=c_list, y=l_list, cv=10)
	joblib.dump(model, 'model.pickle')
	print(f'神经网络算法的平均准确率为: {numpy.mean(score)}')

	# K-Nearest Neighbours  K最近邻分类算法
	# n_neighbors： 使用邻居的数目
	# n_jobs：并行任务数
	model = KNeighborsClassifier(n_neighbors=3, n_jobs=4)
	model.fit(train_X, train_y)
	prediction = model.predict(test_X)
	# print('K近邻分类算法的准确率为: {0}'.format(metrics.accuracy_score(prediction, test_y)))
	score = cross_val_score(model, X=c_list, y=l_list, cv=10)
	print(f'K近邻分类算法的平均准确率为: {numpy.mean(score)}')


def recognition(c_list, l_list, g_list):
	"""
	对未知验证码进行识别
	:param c_list: 数据集
	:param l_list: 标签集
	:param g_list: 待识别验证码
	:return: 识别结果
	"""
	warnings.filterwarnings("ignore")

	train_X = c_list
	train_y = l_list

	test_X = g_list

	model = joblib.load('model.pickle')
	model.fit(train_X, train_y)
	prediction = model.predict(test_X)

	result = ""
	count = 0
	for c in prediction:
		count += 1
		result += c
		if count % 4 == 0 and count != 0:
			result += "\n"

	result = result[:-1]
	return result


def principal_component_analysis(r_character_list):
	"""
	使用主成分分析进行特征提取
	:param r_character_list: 字符列表
	:return:
	"""
	e_list = []
	for n_image in r_character_list:
		image = n_image[1]
		i_height = image.shape[0]
		i_width = image.shape[1]

		n_list = [n_image[0]]
		for i in range(i_height):
			for j in range(i_width):
				n_list.append(image[i, j])

		e_list.append(n_list)

	e_list = pandas.DataFrame(e_list)

	# 从文件中加载模型
	pca = joblib.load('pca.pickle')
	reduced_X = pca.transform(pandas.DataFrame(e_list.iloc[:, 1:]))  # reduced_X为降维后的数据

	name = e_list.iloc[:, 0:1]
	reduced_X = pandas.DataFrame(reduced_X)
	result = pandas.concat([name, reduced_X], axis=1, ignore_index=True)

	return result


def image_recognition():
	"""
	图像识别
	:return:
	"""
	# 读取待识别验证码
	image_list = read_images("./to_be_identified_images")

	# 得到待识别验证码字符特征
	r_character_list = image_digitization(image_list)

	# 特征值提取
	e_character_list = principal_component_analysis(r_character_list)

	# 得到训练集
	characteristics_list, label_list = read_data_from_csv()

	# 机器学习方法测试
	# machine_learning(characteristics_list, label_list)

	# 进行识别
	result = recognition(characteristics_list, label_list, e_character_list.iloc[:, 1:])
	if result is None:
		print("识别失败!")
		exit()

	print(result)


if __name__ == '__main__':
	image_recognition()
