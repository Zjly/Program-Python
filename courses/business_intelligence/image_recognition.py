import os

import pandas
from sklearn.neighbors import KNeighborsClassifier
import warnings

import cv2

from courses.business_intelligence.image_digitization import image_digitization


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


def get_to_be_recognition_list(e_list):
	"""
	将待读入图片字符list转化为DataFrame
	:param e_list:
	:return:
	"""
	g_list = []
	for data in e_list:
		g_list.append(data[1])

	g_list = pandas.DataFrame(g_list)
	return g_list


def read_data_from_csv():
	"""
	从csv文件中读取训练数据
	:return: 数据集，标签集
	"""
	data_list = pandas.read_csv("./data.csv", header=None)

	labels = data_list[0]
	characteristics = data_list.iloc[:, 1:]

	return characteristics, labels


def machine_learning(c_list, l_list, g_list):
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

	# K-Nearest Neighbours  K最近邻分类算法
	model = KNeighborsClassifier(n_neighbors=3)
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


def image_recognition():
	"""
	图像识别
	:return:
	"""
	# 读取待识别验证码
	image_list = read_images("./to_be_identified_images")

	# 得到待识别验证码字符特征
	e_character_list = image_digitization(image_list)

	# 将特征list转化为dataFrame便于识别
	g_list = get_to_be_recognition_list(e_character_list)

	# 得到训练集
	characteristics_list, label_list = read_data_from_csv()

	# 进行识别
	result = machine_learning(characteristics_list, label_list, g_list)
	if result is None:
		print("识别失败!")
		exit()

	print(result)


if __name__ == '__main__':
	image_recognition()
