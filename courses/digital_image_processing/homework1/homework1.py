import cv2
import numpy as np


def grayscale_image(image):
	"""
	进行8位分解图像
	:param image: 原始图像
	:return:
	"""
	# 储存分解图像的数组
	g_image_array = []

	# 对图像的每一位使用位运算进行提取并存入数组
	for i in range(8):
		g_image_array.append(image % 2)
		image = image // 2

	# 将提取后的图像中的0和1分别变为0和255进行二值化
	for i in range(len(g_image_array)):
		g_image_array[i] = g_image_array[i] * 255

		# 显示当前灰度层次的图像
		cv2.namedWindow('demo', 0)
		cv2.imshow("demo", g_image_array[i])
		cv2.waitKey(0)
		cv2.destroyAllWindows()

		# 写入文件
		cv2.imwrite(f"./result/sakura_grayscale_{i}.png", g_image_array[i])

def grayscale_image2(image):
	"""
	查看图像的高4比特和低4比特
	:param image: 原始图像
	:return:
	"""
	# 储存分解图像的数组
	g_image_array = []

	# 对图像的每一位使用位运算进行提取并存入数组
	for i in range(2):
		g_image_array.append(image % 16)
		image = image // 16

	# 将提取后的图像中的0和1分别变为0和255进行二值化
	for i in range(len(g_image_array)):
		g_image_array[i] = g_image_array[i] * 255

		# 显示当前灰度层次的图像
		cv2.namedWindow('demo', 0)
		cv2.imshow("demo", g_image_array[i])
		cv2.waitKey(0)
		cv2.destroyAllWindows()

		# 写入文件
		cv2.imwrite(f"./result/sakura_grayscale(4bit)_{i}.png", g_image_array[i])



def histogram_equalization(image):
	"""
	对图像的直方图进行均衡化
	:param image: 原始图像
	:return:
	"""
	# 灰阶数组
	gray_level_array = np.zeros(256)

	i_height = image.shape[0]
	i_width = image.shape[1]

	# 统计出每个灰阶像素点的个数并存入数组
	for i in range(i_height):
		for j in range(i_width):
			gray_level_array[image[i, j]] += 1

	# 原始直方图数组
	probability_array = np.zeros(256)
	for i in range(256):
		probability_array[i] = gray_level_array[i] / (i_height * i_width)

	# 累计直方图数组
	cumulative_probability_array = np.zeros(256)
	cumulative_probability_array[0] = probability_array[0]

	# 填入累计直方图数组，累计直方图 = 上一灰阶累计直方图 + 当前直方图
	for i in range(1, 256):
		cumulative_probability_array[i] = cumulative_probability_array[i - 1] + probability_array[i]

	# 进行直方图均衡化计算，进行取整扩展
	for i in range(i_height):
		for j in range(i_width):
			image[i, j] = int(cumulative_probability_array[image[i, j]] * 255 + 0.5)

	# 显示直方图均衡化之后的图像
	cv2.namedWindow('demo', 0)
	cv2.imshow("demo", image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	# 写入文件
	cv2.imwrite("./result/west_lake_equalization.png", image)


if __name__ == '__main__':
	# 读入图像
	image_sakura = cv2.imread("./sakura.png", cv2.IMREAD_GRAYSCALE)
	image_west_lake = cv2.imread("./west_lake.png", cv2.IMREAD_GRAYSCALE)

	# 图像8位分解
	grayscale_image(image_sakura)

	# 图像高4比特和低4比特
	grayscale_image2(image_sakura)

	# 图像直方图均衡化
	histogram_equalization(image_west_lake)
