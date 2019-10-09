def arithmetic_mean_filter(image):
	"""
	算数均值滤波器
	:param image: 原始图像
	:return: 算术均值滤波之后的图像
	"""
	am_image = image.copy()

	i_height = am_image.shape[0]
	i_width = am_image.shape[1]

	for i in range(1, i_height - 1):
		for j in range(1, i_width - 1):
			sum_pixel = 0

			# 对该像素周围像素求算数均值
			for x in range(i - 1, i + 2):
				for y in range(j - 1, j + 2):
					sum_pixel += image[x, y]

			am_image[i, j] = int(sum_pixel / 9)

	return am_image


def geometric_mean_filter(image):
	"""
	几何均值滤波器
	:param image: 原始图像
	:return: 几何均值滤波之后的图像
	"""
	gm_image = image.copy()

	i_height = gm_image.shape[0]
	i_width = gm_image.shape[1]

	for i in range(1, i_height - 1):
		for j in range(1, i_width - 1):
			sum_pixel = 1

			# 对该像素周围像素求几何均值
			for x in range(i - 1, i + 2):
				for y in range(j - 1, j + 2):
					sum_pixel *= image[x, y]

			gm_image[i, j] = int(pow(sum_pixel, 1 / 9))

	return gm_image
