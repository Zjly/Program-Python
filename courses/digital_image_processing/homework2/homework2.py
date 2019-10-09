import cv2

from courses.digital_image_processing.homework2.adding_noise import gauss_noise, uniformly_distributed_noise, \
	salt_and_pepper_noise
from courses.digital_image_processing.homework2.wave_filtering import arithmetic_mean_filter, geometric_mean_filter

if __name__ == '__main__':
	# 原始图像
	original_image = cv2.imread("./image.png", cv2.IMREAD_GRAYSCALE)

	# 高斯噪声图像: μ = 0, σ = 20
	gauss_image = gauss_noise(original_image, 0, 20)
	cv2.imwrite("./result/noise_image/gauss_image.png", gauss_image)

	# 均匀分布噪声图像: a = -20, b = 20
	uniform_image = uniformly_distributed_noise(original_image, -20, 20)
	cv2.imwrite("./result/noise_image/uniform_image.png", uniform_image)

	# 椒盐噪声图像:p(a) = 0.1, p(b) = 0.1
	salt_and_pepper_image = salt_and_pepper_noise(original_image, 0.1, 0.1)
	cv2.imwrite("./result/noise_image/salt_and_pepper_image.png", salt_and_pepper_image)

	# 盐噪声图像:p(a) = 0, p(b) = 0.1
	salt_image = salt_and_pepper_noise(original_image, 0, 0.1)
	cv2.imwrite("./result/noise_image/salt_image.png", salt_image)

	# 椒噪声图像:p(a) = 0.1, p(b) = 0
	pepper_image = salt_and_pepper_noise(original_image, 0.1, 0)
	cv2.imwrite("./result/noise_image/pepper_image.png", pepper_image)

	# 算数均值滤波器
	# gauss_image_arithmetic_mean_filter = arithmetic_mean_filter(gauss_image)
	# cv2.imwrite("./result/arithmetic_mean_filter/gauss_image_arithmetic_mean_filter.png",
	# 			gauss_image_arithmetic_mean_filter)
	# uniform_image_arithmetic_mean_filter = arithmetic_mean_filter(uniform_image)
	# cv2.imwrite("./result/arithmetic_mean_filter/uniform_image_arithmetic_mean_filter.png",
	# 			gauss_image_arithmetic_mean_filter)
	# salt_and_pepper_image_arithmetic_mean_filter = arithmetic_mean_filter(salt_and_pepper_image)
	# cv2.imwrite("./result/arithmetic_mean_filter/salt_and_pepper_image_arithmetic_mean_filter.png",
	# 			salt_and_pepper_image_arithmetic_mean_filter)
	# salt_image_arithmetic_mean_filter = arithmetic_mean_filter(salt_image)
	# cv2.imwrite("./result/arithmetic_mean_filter/salt_image_arithmetic_mean_filter.png",
	# 			salt_image_arithmetic_mean_filter)
	# pepper_image_arithmetic_mean_filter = arithmetic_mean_filter(pepper_image)
	# cv2.imwrite("./result/arithmetic_mean_filter/pepper_image_arithmetic_mean_filter.png",
	# 			pepper_image_arithmetic_mean_filter)

	# 几何均值滤波器
	gauss_image_geometric_mean_filter = geometric_mean_filter(gauss_image)

	cv2.namedWindow('demo', 0)
	cv2.imshow("demo", gauss_image_geometric_mean_filter)
	cv2.waitKey(0)
	cv2.destroyAllWindows()