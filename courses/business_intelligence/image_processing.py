import os
import cv2

from courses.business_intelligence.image_digitization import image_digitization, principal_component_analysis, \
	eigenvalue_extraction


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
			name = path.replace("./images\\", "").replace("./test_images\\", "").replace(".jpg", "")
			image = cv2.imread(path)
			image_list.append([name, image])

	return image_list


def save_data_to_csv(data_list):
	"""
	将数据存入csv文件中
	:param data_list: 特征列表
	:return:
	"""
	data_list.to_csv("data.csv", sep=",", header=False, index=False)


def image_processing():
	"""
	图像处理
	:return:
	"""
	# 读取验证码列表
	img_list = read_images('./images')

	# 字符列表
	r_character_list = image_digitization(img_list)

	# 特征值提取
	e_character_list = principal_component_analysis(r_character_list)

	# 存入csv文件中
	save_data_to_csv(e_character_list)


if __name__ == '__main__':
	image_processing()
