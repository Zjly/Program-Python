import numpy


def euclidean_distance(points):
	"""
	计算各点之间的欧式距离
	:param points: 各点坐标矩阵
	:return:
	"""
	print("各点之间的欧氏距离为: ", end="")
	# 对点进行两两计算
	for i in range(len(points) - 1):
		for j in range(i + 1, len(points)):
			# 求出两点的差
			difference = points[i] - points[j]
			# 根据欧氏距离的公式计算
			distance = numpy.sqrt(numpy.dot(difference, difference.T))
			print(round(distance, 4), end="    ")
	print()


def mahalanobis_distance(points):
	"""
	计算各点之间的马氏距离
	:param points: 各点坐标矩阵
	:return:
	"""
	# 协方差矩阵
	cov = numpy.cov(points.T)
	# 协方差矩阵的逆
	inv = numpy.linalg.inv(cov)

	print("各点之间的马氏距离为: ", end="")
	for i in range(len(points) - 1):
		for j in range(i + 1, len(points)):
			difference = points[i] - points[j]
			# 根据马氏距离的公式计算
			distance = numpy.sqrt(numpy.dot(numpy.dot(difference, inv), difference.T))
			print(round(distance, 4), end="    ")
	print()


if __name__ == '__main__':
	euclidean_distance(numpy.array([[0, 0], [1, 1], [0, 1], [1, 0]]))
	mahalanobis_distance(numpy.array([[0, 0], [1, 1], [0, 1], [1, 0]]))
