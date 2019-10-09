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


def arithmetic_mean_filter(image):
	"""
	算数均值滤波器
	:param image: 原始图像
	:return: 算术均值滤波之后的图像
	"""
	am_image = image.copy()

	i_height = am_image.shape[0]
	i_width = am_image.shape[1]

	for i in range(i_height):
		for j in range(i_width):
			sum_pixel = 0
			count_pixel = 0

			# 对该像素周围像素求算数均值
			for x in range(i - 1, i + 2):
				for y in range(j - 1, j + 2):
					if is_in_range(x, y, i_height, i_width):
						sum_pixel += image[x, y]
						count_pixel += 1

			am_image[i, j] = int(sum_pixel / count_pixel)

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

	for i in range(i_height):
		for j in range(i_width):
			product_pixel = 1
			count_pixel = 0

			# 对该像素周围像素求几何均值
			for x in range(i - 1, i + 2):
				for y in range(j - 1, j + 2):
					if is_in_range(x, y, i_height, i_width):
						# 如若该点像素值为0则积*1，避免乘积直接变为0
						if int(image[x, y]) == 0:
							product_pixel *= 1
						else:
							product_pixel *= int(image[x, y])
						count_pixel += 1

			gm_image[i, j] = int(pow(product_pixel, 1 / count_pixel))

	return gm_image


def harmonic_mean_filter(image):
	"""
	谐波均值滤波器
	:param image: 原始图像
	:return: 谐波均值滤波之后的图像
	"""
	hm_image = image.copy()

	i_height = hm_image.shape[0]
	i_width = hm_image.shape[1]

	for i in range(i_height):
		for j in range(i_width):
			sum_pixel = 0
			count_pixel = 0

			# 进行谐波均值滤波计算
			for x in range(i - 1, i + 2):
				for y in range(j - 1, j + 2):
					if is_in_range(x, y, i_height, i_width):
						# 如若该点像素值为0则和+1，避免除零错误
						if image[x, y] == 0:
							sum_pixel += 1
						else:
							sum_pixel += 1 / image[x, y]

						count_pixel += 1

			image_pixel = int(count_pixel / sum_pixel)

			# 将像素值保持在[0, 255]之间
			if 0 <= image_pixel <= 255:
				hm_image[i, j] = image_pixel
			elif image_pixel < 0:
				hm_image[i, j] = 0
			elif image_pixel > 255:
				hm_image[i, j] = 255

	return hm_image


def inverse_harmonic_mean_filter(image, Q):
	"""
	逆谐波均值滤波器
	:param Q: 阶数
	:param image: 原始图像
	:return: 逆谐波均值滤波之后的图像
	"""
	ihm_image = image.copy()

	i_height = ihm_image.shape[0]
	i_width = ihm_image.shape[1]

	for i in range(i_height):
		for j in range(i_width):
			molecule = 0
			denominator = 0

			# 进行逆谐波均值滤波计算
			for x in range(i - 1, i + 2):
				for y in range(j - 1, j + 2):
					if is_in_range(x, y, i_height, i_width):
						pixel = int(image[x, y])

						# 设置像素为0的点为1，避免0的负指数的错误
						if pixel == 0:
							pixel = 1

						molecule += pow(pixel, Q + 1)
						denominator += pow(pixel, Q)

			ihm_image[i, j] = int(molecule / denominator)

	return ihm_image


def maximum_filter(image):
	"""
	最大值滤波器
	:param image: 原始图像
	:return: 最大值滤波后的图像
	"""
	m_image = image.copy()

	i_height = m_image.shape[0]
	i_width = m_image.shape[1]

	for i in range(i_height):
		for j in range(i_width):
			max_pixel = 0

			# 进行最大值滤波计算
			for x in range(i - 1, i + 2):
				for y in range(j - 1, j + 2):
					if is_in_range(x, y, i_height, i_width):
						if image[x, y] > max_pixel:
							max_pixel = image[x, y]

			m_image[i, j] = max_pixel

	return m_image


def minimum_filter(image):
	"""
	最小值滤波器
	:param image: 原始图像
	:return: 最小值滤波后的图像
	"""
	m_image = image.copy()

	i_height = m_image.shape[0]
	i_width = m_image.shape[1]

	for i in range(i_height):
		for j in range(i_width):
			min_pixel = 255

			# 进行最小值滤波计算
			for x in range(i - 1, i + 2):
				for y in range(j - 1, j + 2):
					if is_in_range(x, y, i_height, i_width):
						if image[x, y] < min_pixel:
							min_pixel = image[x, y]

			m_image[i, j] = min_pixel

	return m_image


def median_filter(image):
	"""
	中值滤波器
	:param image: 原始图像
	:return: 中值滤波之后的图像
	"""
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
						array.append(image[x, y])

			# 对周围像素进行排序
			array.sort()

			# 取中值作为该像素的值
			m_image[i, j] = array[int((len(array) - 1) / 2)]

	return m_image


def adaptive_median_filter(image):
	"""
	自适应中值滤波器
	:param image: 原始图像
	:return: 自适应中值滤波后的图像
	"""
	am_image = image.copy()

	i_height = am_image.shape[0]
	i_width = am_image.shape[1]

	for i in range(i_height):
		for j in range(i_width):
			# 当前模板尺寸，直至最大尺寸为止
			size = 3
			max_size = 7

			while True:
				# 放大边界数
				delta = int((size - 1) / 2)

				# 像素数组
				array = []
				# 将像素置入像素数组
				for x in range(i - delta, i + delta + 1):
					for y in range(j - delta, j + delta + 1):
						if is_in_range(x, y, i_height, i_width):
							array.append(image[x, y])

				array.sort()

				z_min = int(array[0])
				z_max = int(array[len(array) - 1])
				z_med = int(array[int(len(array) / 2)])
				z_xy = int(image[i, j])

				# A层次，判断z_med是否为脉冲
				a1 = z_med - z_min
				a2 = z_med - z_max

				if not (a1 > 0 and a2 < 0):
					# 模板尺寸还可以放大
					if size < max_size:
						size += 2
						continue
					else:
						am_image[i, j] = z_med
						break

				# B层次，判断z_xy本身是否为脉冲
				b1 = z_xy - z_min
				b2 = z_xy - z_max

				if b1 > 0 and b2 < 0:
					am_image[i, j] = z_xy
					break
				else:
					am_image[i, j] = z_med
					break

	return am_image
