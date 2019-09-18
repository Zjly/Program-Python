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


def mahalanobis_distance1(points):
	"""
	计算矩阵之间各向量之间的马氏距离
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
			# 两点之差
			difference = points[i] - points[j]
			# 根据马氏距离的公式计算
			distance = numpy.sqrt(numpy.dot(numpy.dot(difference, inv), difference.T))
			print(round(distance, 4), end="    ")
	print()


def mahalanobis_distance2(matrix, vector):
	"""
	计算向量到矩阵的马氏距离
	:return:
	"""
	# 各特征的算术平均值
	mean = numpy.mean(matrix, axis=0)
	# 协方差矩阵
	cov = numpy.cov(matrix.T)
	# 协方差矩阵的逆
	inv = numpy.linalg.inv(cov)

	print("各向量到矩阵的马氏距离为: ", end="")
	# 对向量数组中的每一个向量进行对矩阵的马氏距离计算
	for vect in vector:
		# 两者之差
		difference = vect - mean
		# 根据马氏距离的公式计算
		distance = numpy.sqrt(numpy.dot(numpy.dot(difference, inv), difference.T))
		print(round(distance, 4), end="    ")
	print()


if __name__ == '__main__':
	X1 = numpy.array([[0, 0], [0, 1], [1, 0], [1, 1]])
	X2 = numpy.array([[0.052, 0.084, 0.021], [0.037, 0.0071, 0.022], [0.041, 0.055, 0.11], [0.11, 0.021, 0.0073],
					  [0.030, 0.112, 0.072], [0.16, 0.056, 0.021], [0.074, 0.083, 0.105], [0.19, 0.02, 1]])

	# 欧式距离计算
	euclidean_distance(X1)

	# 各点之间的马氏距离计算
	mahalanobis_distance1(X1)

	# 向量到矩阵的马氏距离计算
	mahalanobis_distance2(X2, X2)
