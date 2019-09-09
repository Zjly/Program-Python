import os
from datetime import datetime
import numpy
import pymysql
import pandas
import sklearn
import tflearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
import warnings

from tflearn.data_utils import to_categorical


def read_data_from_database():
	"""
	从数据库中读取特征数据
	:return: 由[字符, 特征数据]组成的DataFrame
	"""
	db = pymysql.connect("localhost", "root", "root", "verification_code")
	cursor = db.cursor()
	sql = "select * from character_data"
	cursor.execute(sql)
	result = cursor.fetchall()
	data = pandas.DataFrame(list(result))
	data.columns = ["character", "data0", "data1", "data2", "data3", "data4", "data5", "data6", "data7", "data8",
					"data9", "data10", "data11", "data12", "data13", "data14", "data15"]
	return data


def machine_learning(data):
	"""
	多种机器学习方式测试
	:param data: 数据集
	:return:
	"""
	warnings.filterwarnings("ignore")

	X = data[["data0", "data1", "data2", "data3", "data4", "data5", "data6", "data7", "data8", "data9", "data10",
			  "data11", "data12", "data13", "data14", "data15"]]
	y = data["character"]

	train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3)

	# 支持向量机
	model = svm.SVC()
	model.fit(train_X, train_y)
	prediction = model.predict(test_X)
	print('The accuracy of the SVM is: {0}'.format(sklearn.metrics.accuracy_score(prediction, test_y)))

	# 逻辑回归
	model = LogisticRegression()
	model.fit(train_X, train_y)
	prediction = model.predict(test_X)
	print('The accuracy of the Logistic Regression is: {0}'.format(metrics.accuracy_score(prediction, test_y)))

	# Decision Tree 决策树
	model = DecisionTreeClassifier()
	model.fit(train_X, train_y)
	prediction = model.predict(test_X)
	print('The accuracy of the Decision Tree is: {0}'.format(metrics.accuracy_score(prediction, test_y)))

	# K-Nearest Neighbours  K最近邻分类算法
	model = KNeighborsClassifier(n_neighbors=3)
	model.fit(train_X, train_y)
	prediction = model.predict(test_X)
	print('The accuracy of the KNN is: {0}'.format(metrics.accuracy_score(prediction, test_y)))


def DNN(data):
	"""
	神经网络模型训练
	:param data: 数据集
	:return:
	"""
	X = data[["data0", "data1", "data2", "data3", "data4", "data5", "data6", "data7", "data8", "data9", "data10",
			  "data11", "data12", "data13", "data14", "data15"]]
	y = data["character"]

	X = numpy.array(X)

	random_state = 1
	train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.1, random_state=random_state)

	unique_y_labels = list(train_y.value_counts().index)
	le = sklearn.preprocessing.LabelEncoder()
	le.fit(unique_y_labels)
	no_of_unique_y_labels = len(unique_y_labels)

	train_y = to_categorical(train_y.map(lambda x: le.transform([x])[0]), nb_classes=len(unique_y_labels))
	test_y = to_categorical(test_y.map(lambda x: le.transform([x])[0]), nb_classes=len(unique_y_labels))

	n_epoch = 1000
	net = tflearn.input_data([None, 16])
	net = tflearn.embedding(net, input_dim=10000, output_dim=128)
	net = tflearn.lstm(net, 128, dropout=0.8)
	net = tflearn.fully_connected(net, no_of_unique_y_labels, activation='softmax')
	net = tflearn.regression(net, optimizer='adam', learning_rate=0.001, loss='categorical_crossentropy')
	model = tflearn.DNN(net, tensorboard_verbose=0, tensorboard_dir="./tflearn_data/tflearn_logs/")
	model.fit(train_X, train_y, validation_set=(test_X, test_y), n_epoch=n_epoch, show_metric=True, batch_size=42)
	time = datetime.now()
	time_str = str(time).replace(":", ".")
	os.makedirs(f"./tflearn_data/tflearn_models/{time_str}({n_epoch}, {random_state})")
	model.save(f"./tflearn_data/tflearn_models/{time_str}({n_epoch}, {random_state})/model")


if __name__ == '__main__':
	data_list = read_data_from_database()
# machine_learning(data_list)
# DNN(data_list)
