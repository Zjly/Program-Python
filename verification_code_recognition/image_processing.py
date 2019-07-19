import os
import cv2


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
			name = path.replace("./images\\", "").replace(".jpg", "")
			image = cv2.imread(path)
			image_list.append([name, image])

	return image_list


def gray_scale(image_list):
	"""
	图像灰度化
	:param image_list: 图像列表
	:return: 灰度化之后的图像列表
	"""
	gray_image_list = []
	for image in image_list:
		gray_image = cv2.cvtColor(image[1], cv2.COLOR_BGR2GRAY)
		gray_image_list.append([image[0], gray_image])

	return gray_image_list


def binarization(image_list):
	"""
	图像二值化
	:param image_list: 图像列表
	:return: 二值化之后的图像列表
	"""
	binarization_image_list = []
	for image in image_list:
		# 大律法，全局自适应阈值 参数0可改为任意数字但不起作用
		ret, binarization_image = cv2.threshold(image[1], 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
		binarization_image_list.append([image[0], binarization_image])

	return binarization_image_list


def noise_processing(image_list, threshold, times):
	"""
	噪点处理
	:param image_list: 图像列表
	:param threshold: 阈值 代表一个点周围n个点颜色与之不同则更改该点的颜色
	:param times: 算法调用的次数
	:return: 去除噪点后的图像列表
	"""
	for i in range(times):
		image_list = remove_noise(image_list, threshold)

	return image_list


def remove_noise(image_list, threshold):
	"""
	去除图像噪点
	:param image_list: 图像列表
	:param threshold: 阈值 代表一个点周围n个点颜色与之不同则更改该点的颜色
	:return: 去除噪点后的图像列表
	"""
	for image in image_list:
		image = image[1]
		i_height = image.shape[0]
		i_width = image.shape[1]

		# 横向边框设定
		for i in range(i_width):
			image[0, i] = 255
			image[i_height - 1, i] = 255

		# 纵向边框设定
		for i in range(i_height):
			image[i, 0] = 255
			image[i, i_width - 1] = 255

		for i in range(1, i_height - 1):
			for j in range(1, i_width - 1):
				i_value = image[i, j]

				# 去除黑点周围噪点
				if i_value == 0:
					i_count = 0
					for m in range(i - 1, i + 2):
						for n in range(j - 1, j + 2):
							if image[m, n] == 255:
								i_count = i_count + 1
					if i_count >= threshold:
						image[i, j] = 255
				else:
					i_count = 0
					for m in range(i - 1, i + 2):
						for n in range(j - 1, j + 2):
							if image[m, n] == 0:
								i_count = i_count + 1
					if i_count >= threshold:
						image[i, j] = 0
	return image_list


def image_processing():
	"""
	图像处理
	:return:
	"""
	img_list = read_images('./test_image')
	g_img_list = gray_scale(img_list)
	b_img_list = binarization(g_img_list)
	n_image_list = noise_processing(b_img_list, 7, 2)


if __name__ == '__main__':
	image_processing()
