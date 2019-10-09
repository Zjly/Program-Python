import cv2

from courses.digital_image_processing.homework2.adding_noise import gauss_noise, uniformly_distributed_noise, \
	salt_and_pepper_noise
from courses.digital_image_processing.homework2.wave_filtering import arithmetic_mean_filter, geometric_mean_filter, \
	harmonic_mean_filter, inverse_harmonic_mean_filter, maximum_filter, minimum_filter, median_filter, \
	adaptive_median_filter


def add_noise():
	"""
	向图像添加噪声
	:return:
	"""
	image_list = []

	# 原始图像
	original_image = cv2.imread("./image.png", cv2.IMREAD_GRAYSCALE)

	# 高斯噪声图像: μ = 0, σ = 20
	gauss_image = gauss_noise(original_image, 0, 20)
	cv2.imwrite("./noise_image/gauss_image.png", gauss_image)
	image_list.append(["gauss_image", gauss_image])

	# 均匀分布噪声图像: a = -20, b = 20
	uniform_image = uniformly_distributed_noise(original_image, -20, 20)
	cv2.imwrite("./noise_image/uniform_image.png", uniform_image)
	image_list.append(["uniform_image", uniform_image])

	# 椒噪声图像:p(a) = 0.1, p(b) = 0
	pepper_image = salt_and_pepper_noise(original_image, 0.1, 0)
	cv2.imwrite("./noise_image/pepper_image.png", pepper_image)
	image_list.append(["pepper_image", pepper_image])

	# 盐噪声图像:p(a) = 0, p(b) = 0.1
	salt_image = salt_and_pepper_noise(original_image, 0, 0.1)
	cv2.imwrite("./noise_image/salt_image.png", salt_image)
	image_list.append(["salt_image", salt_image])

	# 椒盐噪声图像:p(a) = 0.1, p(b) = 0.1
	salt_and_pepper_image_10 = salt_and_pepper_noise(original_image, 0.1, 0.1)
	cv2.imwrite("./noise_image/salt_and_pepper_image_p(0.1).png", salt_and_pepper_image_10)
	image_list.append(["salt_and_pepper_image_p(0.1)", salt_and_pepper_image_10])

	# 椒盐噪声图像:p(a) = 0.25, p(b) = 0.25
	salt_and_pepper_image_25 = salt_and_pepper_noise(original_image, 0.25, 0.25)
	cv2.imwrite("./noise_image/salt_and_pepper_image_p(0.25).png", salt_and_pepper_image_25)
	image_list.append(["salt_and_pepper_image_p(0.25)", salt_and_pepper_image_25])

	return image_list


def wave_filter(image_list):
	"""
	滤波处理
	:param image_list: 图片列表
	:return:
	"""
	for images in image_list:
		image_name = images[0]
		image = images[1]

		# 算数均值滤波器
		cv2.imwrite(f"./result/arithmetic_mean_filter/{image_name}.png", arithmetic_mean_filter(image))

		# 几何均值滤波器
		cv2.imwrite(f"./result/geometric_mean_filter/{image_name}.png", geometric_mean_filter(image))

		# 谐波均值滤波器
		cv2.imwrite(f"./result/harmonic_mean_filter/{image_name}.png", harmonic_mean_filter(image))

		# 逆谐波均值滤波器
		cv2.imwrite(f"./result/inverse_harmonic_mean_filter/{image_name}_1.5.png",
					inverse_harmonic_mean_filter(image, 1.5))
		cv2.imwrite(f"./result/inverse_harmonic_mean_filter/{image_name}_-1.5.png",
					inverse_harmonic_mean_filter(image, -1.5))

		# 最大值滤波器
		cv2.imwrite(f"./result/maximum_filter/{image_name}.png", maximum_filter(image))

		# 最小值滤波器
		cv2.imwrite(f"./result/minimum_filter/{image_name}.png", minimum_filter(image))

		# 中值滤波器
		cv2.imwrite(f"./result/median_filter/{image_name}.png", median_filter(image))

		# 自适应中值滤波器
		cv2.imwrite(f"./result/adaptive_median_filter/{image_name}.png", adaptive_median_filter(image))


if __name__ == '__main__':
	# 添加噪声
	img_list = add_noise()

	# 图像滤波
	wave_filter(img_list)
