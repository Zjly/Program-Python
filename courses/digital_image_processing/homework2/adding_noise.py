import numpy as np
import cv2
import random


def gauss_noise(image, means, sigma):
	"""
	添加高斯噪声
	:param image: 原图像
	:param means: 均值μ
	:param sigma: 标准差σ
	:return: 添加高斯噪声后的图像
	"""
	i_height = image.shape[0]
	i_width = image.shape[1]

	for i in range(i_height):
		for j in range(i_width):
			# 计算高斯噪声的值
			gauss_num = random.gauss(means, sigma)
			gauss_pixel = image[i, j] + gauss_num

			# 添加高斯噪声，并将像素值保持在[0, 255]之间
			if gauss_pixel < 0:
				image[i, j] = 0
			elif gauss_pixel > 255:
				image[i, j] = 255
			else:
				image[i, j] = gauss_pixel

	return image

def uniformly_distributed_noise(image):


if __name__ == '__main__':
	original_image = cv2.imread("./image.png", cv2.IMREAD_GRAYSCALE)
	gauss_image = gauss_noise(original_image, 0, 20)

	cv2.namedWindow('demo', 0)
	cv2.imshow("demo", gauss_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
