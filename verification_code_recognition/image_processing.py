import os
import cv2
import numpy


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
			name = path.replace("./images\\", "").replace("./test_image\\", "").replace(".jpg", "")
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
	for n_image in image_list:
		image = n_image[1]
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

		# 判定每一个像素
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


# 黑点的个数，通过与一个阈值的比较，确定是噪点还是字母
num = 0

def fill_color(image_list):
	"""
	向字母中填充颜色
	:param image_list: 图像列表
	:return: 颜色填充完毕的图像列表
	"""
	global num

	# 此处设置f_image_list是为了保存正确的四个字母的验证码，由于下方代码使用的是foreach，故不能在原list中使用remove，所以采用了添加到新list的方法
	f_image_list = []

	for n_image in image_list:
		image = n_image[1]
		i_height = image.shape[0]
		i_width = image.shape[1]

		# 待填充颜色
		color = 0
		colors = [0, 0, 0, 0]
		result_num = 0

		# 对向量黑点进行填充数字 这里需要从左到右扫描
		for j in range(i_width):
			for i in range(i_height):
				if image[i, j] == 0:
					num = 0
					color += 1
					overflow_filling(image, i, j, color)

					# 过滤噪点的颜色填充 TODO 此处需要处理一下分割出超过4个字母的部分 目前只是暂且屏蔽
					if num > 20 and result_num < 4:
						colors[result_num] = color
						result_num += 1

		n_image.append(colors)

		# 过滤掉未识别出4个字母的图片
		if colors[3] != 0:
			f_image_list.append(n_image)

	return f_image_list


def overflow_filling(image, x, y, color):
	"""
	对方块及其四周进行递归漫水填充
	:param image: 图像
	:param x: 当前像素横坐标
	:param y: 当前像素纵坐标
	:param color: 待填充颜色
	:return:
	"""
	global num
	if image[x, y] == 0:
		image[x, y] = color
		num += 1

		# 递归调用对四周方块进行填充
		overflow_filling(image, x - 1, y, color)
		overflow_filling(image, x + 1, y, color)
		overflow_filling(image, x, y - 1, color)
		overflow_filling(image, x, y + 1, color)

		overflow_filling(image, x - 1, y - 1, color)
		overflow_filling(image, x - 1, y, color)
		overflow_filling(image, x - 1, y, color)
		overflow_filling(image, x - 1, y, color)


def divide_characters(image_list):
	"""
	分隔字符
	:param image_list: 图像列表
	:return: 单个字符组成的[名字，矩阵]列表
	"""
	d_list = []

	for n_image in image_list:
		image = n_image[1]
		i_height = image.shape[0]
		i_width = image.shape[1]

		c_num = 0
		# 对每一种颜色的字符进行提取
		for color in n_image[2]:
			left = i_width
			right = 0
			up = i_height
			down = 0

			# 找出该字符的边界
			for i in range(i_height):
				for j in range(i_width):
					if image[i, j] == color:
						if j < left:
							left = j

						if j > right:
							right = j

						if i < up:
							up = i

						if i > down:
							down = i

			width = right - left + 1
			height = down - up + 1

			p_image = numpy.zeros([height, width])

			# 分离出字符
			for i in range(height):
				for j in range(width):
					if image[i + up, j + left] == color:
						p_image[i, j] = 1

			# 保存图片名字和图片到end_image中
			end_image = [n_image[0][c_num], p_image]
			c_num += 1

			d_list.append(end_image)

	return d_list

def rotate_character(c_list):
	"""
	旋转字符
	:param c_list: 字符列表
	:return: 旋转完毕后的字符列表
	"""

def image_processing():
	"""
	图像处理
	:return:
	"""
	# 读取验证码列表
	img_list = read_images('./images')

	# 图像灰度化
	g_img_list = gray_scale(img_list)

	# 图像二值化
	b_img_list = binarization(g_img_list)

	# 图像去除噪点
	n_image_list = noise_processing(b_img_list, 7, 2)

	# 填充图像字母
	f_image_list = fill_color(n_image_list)

	# 分离各个字符并存入数组
	character_list = divide_characters(f_image_list)

	print()


if __name__ == '__main__':
	image_processing()
