from fractions import Fraction


def question1():
	bag = [2, 3, 6, 13, 29, 61]
	b_bag = []

	for i in bag:
		b_bag.append(i * 17 % 157)

	for i in b_bag:
		print(i, end=" ")

	print()
	print(202 * 37 % 157)
	print(137 * 37 % 157)

def question2():
	print(6 ** 29 % 91)

def question3():
	x1 = Fraction(7)
	y1 = Fraction(9)
	x2 = Fraction(7)
	y2 = Fraction(9)

	l1 = (3 * x1 ** 2 + 1) / (2 * y1)
	x3 = l1 ** 2 - x1 - x2
	y3 = (x1 - x3) * l1 - y1
	print(l1, x3, y3)
	print(float(l1), float(x3), float(y3))

	l2 = (y3 - y1) / (x3 - x1)
	x4 = l2 ** 2 - x1 - x3
	y4 = (x1 - x4) * l2 - y1
	print(l2, x4, y4)
	print(float(l2), float(x4), float(y4))

def question4():
	n = 11
	g = 2
	x = 3
	y = 2
	X = g ** x % n
	Y = g ** y % n
	k1 = Y ** x % n
	k2 = X ** y % n
	print(X, Y, k1, k2)

if __name__ == '__main__':
	question4()
