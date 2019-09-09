import numpy


def question1():
	"""
	若X=[2 3], Y=[3 1], 求COV(X,Y)
	:return:
	"""
	x = numpy.array([2, 3])
	y = numpy.array([3, 1])
	print("1.\nCOV(X,Y): \n", numpy.cov(x, y), end="\n\n")


def question2():
	"""
	已知X=[[4 5 1], [3 1 0], [2 3 2]], 求X的逆, COV(X)
	:return:
	"""
	x = numpy.array([[4, 5, 1], [3, 1, 0], [2, 3, 2]])
	print("2.\nX的逆矩阵: \n", numpy.linalg.inv(x))
	print("COV(X): \n", numpy.cov(x), end="\n\n")


def question3():
	"""
	有一个二类问题，其判别函数为g(X)=3x1+5x2-6x3-2。试将下面三个模式分别进行分类：X1=[4 7 1]T,X2=[1 -5 2]T,X3=[4 4 5]T
	:return:
	"""

	def g(x1, x2, x3):
		return 3 * x1 + 5 * x2 - 6 * x3 - 2

	X1 = g(4, 7, 1)
	X2 = g(1, -5, 2)
	X3 = g(4, 4, 5)
	print(f"3.\n由于g(X1) = {X1}, g(X2) = {X2}, g(X3) = {X3}, 故X1属于ω1, X2属于ω2, X3无法判别归属")


if __name__ == '__main__':
	question1()
	question2()
	question3()
