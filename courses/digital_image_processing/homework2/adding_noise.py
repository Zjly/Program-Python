import random


def gauss_noise(image, means, sigma):
	"""
	添加高斯噪声
	:param image: 原图像
	:param means: 均值μ
	:param sigma: 标准差σ
	:return: 添加高斯噪声后的图像
	"""
	g_image = image.copy()

	i_height = g_image.shape[0]
	i_width = g_image.shape[1]

	for i in range(i_height):
		for j in range(i_width):
			# 计算高斯噪声的值
			gauss_num = random.gauss(means, sigma)
			gauss_pixel = g_image[i, j] + gauss_num

			# 添加高斯噪声，并将像素值保持在[0, 255]之间
			if gauss_pixel < 0:
				g_image[i, j] = 0
			elif gauss_pixel > 255:
				g_image[i, j] = 255
			else:
				g_image[i, j] = gauss_pixel

	return g_image


def uniformly_distributed_noise(image, a, b):
	"""
	添加均匀分布噪声
	:param image: 原图像
	:param a: 最小值
	:param b: 最大值
	:return: 添加均匀分布噪声后的图像
	"""
	u_image = image.copy()

	i_height = u_image.shape[0]
	i_width = u_image.shape[1]

	for i in range(i_height):
		for j in range(i_width):
			# 计算均匀分布噪声的值
			uniform_num = random.uniform(a, b)
			uniform_pixel = u_image[i, j] + uniform_num

			# 添加均匀分布噪声，并将像素值保持在[0, 255]之间
			if uniform_pixel < 0:
				u_image[i, j] = 0
			elif uniform_pixel > 255:
				u_image[i, j] = 255
			else:
				u_image[i, j] = uniform_pixel

	return u_image


def salt_and_pepper_noise(image, pa, pb):
	"""
	添加椒盐噪声
	:param image: 原图像
	:param pa: 椒噪声概率
	:param pb: 盐噪声概率
	:return: 添加椒盐噪声后的图像
	"""
	sp_image = image.copy()

	i_height = sp_image.shape[0]
	i_width = sp_image.shape[1]

	for i in range(i_height):
		for j in range(i_width):
			# 随机数，与椒盐噪声概率比较后决定其是椒噪声还是盐噪声
			sp_num = random.random()

			if sp_num < pa:
				sp_image[i, j] = 0
			elif sp_num > 1 - pb:
				sp_image[i, j] = 255

	return sp_image
