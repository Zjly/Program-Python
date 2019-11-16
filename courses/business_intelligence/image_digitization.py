import warnings

import cv2
import numpy
import pandas
from sklearn.decomposition import PCA
import joblib


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


def noise_processing(image_list):
	"""
	噪点处理
	:param image_list: 图像列表
	:return: 去除噪点后的图像列表
	"""
	for n_image in image_list:
		image = n_image[1]

		m_image = image.copy()

		i_height = m_image.shape[0]
		i_width = m_image.shape[1]

		for i in range(i_height):
			for j in range(i_width):
				array = []

				# 进行中值滤波计算
				for x in range(i - 1, i + 2):
					for y in range(j - 1, j + 2):
						if is_in_range(x, y, i_height, i_width):
							array.append(m_image[x, y])

				# 对周围像素进行排序
				array.sort()

				# 取中值作为该像素的值
				image[i, j] = array[int((len(array) - 1) / 2)]

	return image_list


def is_in_range(x, y, height, width):
	"""
	该像素是否在图像中
	:param x: 像素X坐标
	:param y: 像素Y坐标
	:param height: 图像高度
	:param width: 图像宽度
	:return: 像素是否在图像中
	"""
	if x < 0 or x >= height:
		return False

	if y < 0 or y >= width:
		return False

	return True


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

					# 过滤噪点的颜色填充
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
	if x < 30 and y < 120 and image[x, y] == 0:
		image[x, y] = color
		num += 1

		# 递归调用对四周方块进行填充
		overflow_filling(image, x - 1, y, color)
		overflow_filling(image, x + 1, y, color)
		overflow_filling(image, x, y - 1, color)
		overflow_filling(image, x, y + 1, color)


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
			p_image.fill(255)

			# 分离出字符
			for i in range(height):
				for j in range(width):
					if image[i + up, j + left] == color:
						p_image[i, j] = 0

			# 保存图片名字和图片到end_image中
			end_image = [n_image[0][c_num], p_image]
			c_num += 1

			d_list.append(end_image)

	return d_list


def rotate_character(image_list):
	"""
	旋转字符
	:param image_list: 字符列表
	:return: 旋转完毕后的字符列表
	"""
	r_list = []
	for n_image in image_list:
		image = n_image[1]
		i_height = image.shape[0]
		i_width = image.shape[1]

		# 这里需要对图片进行一个转化为数对的处理 方便接下来调用minAreaRect函数
		r_image = numpy.array([0, 0])
		for i in range(i_height):
			for j in range(i_width):
				if image[i, j] == 0:
					point = numpy.array([i, j])
					r_image = numpy.vstack((r_image, point))
		r_image = r_image[1:]

		# 最小外接矩形
		rect_image = cv2.minAreaRect(r_image)

		# 矩形的四个顶点
		box = cv2.boxPoints(rect_image)
		box = numpy.int0(box)

		# 旋转角度
		angle = cv2.minAreaRect(r_image)[2]
		if angle > 45:
			angle = 135 - angle
		elif angle < -45:
			angle = angle + 90

		center = (i_width // 2, i_height // 2)

		# 获得图像绕着某一点的旋转矩阵
		matrix = cv2.getRotationMatrix2D(center, -angle, 1.0)

		# 进行仿射变换
		rotated = cv2.warpAffine(image, matrix, (i_width, i_height), flags=cv2.INTER_CUBIC,
								 borderMode=cv2.BORDER_REPLICATE)

		# 统一缩放图像到16*16
		f_image = cv2.resize(rotated, (16, 16), interpolation=cv2.INTER_LANCZOS4)

		# 将变换完成后的图像进行二值化
		for i in range(f_image.shape[0]):
			for j in range(f_image.shape[1]):
				if f_image[i, j] > 180:
					f_image[i, j] = 1
				else:
					f_image[i, j] = 0

		# cv2.namedWindow('image', cv2.WINDOW_KEEPRATIO)
		# cv2.imshow("image", f_image)
		# cv2.waitKey(0)
		# cv2.destroyAllWindows()

		r_list.append([n_image[0], f_image])

	return r_list


def eigenvalue_extraction(image_list):
	"""
	对字符图片进行特征值提取，划分为16个区域并计算每一个区域内的像素个数
	:param image_list: 图像列表
	:return: 标记，字母的特征值列表
	"""
	e_list = []
	for n_image in image_list:
		image = n_image[1]
		i_height = image.shape[0]
		i_width = image.shape[1]

		n_list = [0] * 17
		n_list[0] = n_image[0]
		for i in range(i_height):
			for j in range(i_width):
				# 获取索引
				index = int(i / 4) * 4 + int(j / 4) + 1
				# 加入指定的数组图像块中
				if image[i, j] == 0:
					n_list[index] += 1

		e_list.append(n_list)

	e_list = pandas.DataFrame(e_list)

	return e_list


def principal_component_analysis(image_list):
	"""
	使用主成分分析对数据进行降维
	:param image_list: 图像列表
	:return: 标记，字母的特征值列表
	"""
	e_list = []
	for n_image in image_list:
		image = n_image[1]
		i_height = image.shape[0]
		i_width = image.shape[1]

		n_list = [n_image[0]]
		for i in range(i_height):
			for j in range(i_width):
				n_list.append(image[i, j])

		e_list.append(n_list)

	e_list = pandas.DataFrame(e_list)

	pca = PCA(n_components='mle')
	pca.fit(pandas.DataFrame(e_list.iloc[:, 1:]))

	# 保存模型
	joblib.dump(pca, 'pca.pickle')
	reduced_X = pca.transform(pandas.DataFrame(e_list.iloc[:, 1:]))  # reduced_X为降维后的数据

	name = e_list.iloc[:, 0:1]
	reduced_X = pandas.DataFrame(reduced_X)
	result = pandas.concat([name, reduced_X], axis=1, ignore_index=True)

	return result


def image_digitization(img_list):
	"""
	图像数字化
	:return: 字符特征值矩阵列表
	"""
	# 图像灰度化
	g_img_list = gray_scale(img_list)

	# 图像二值化
	b_img_list = binarization(g_img_list)

	# 图像去除噪点
	n_img_list = noise_processing(b_img_list)

	# 填充图像字母
	f_img_list = fill_color(n_img_list)

	# 分离各个字符
	character_list = divide_characters(f_img_list)

	# 旋转字符
	r_character_list = rotate_character(character_list)

	return r_character_list
