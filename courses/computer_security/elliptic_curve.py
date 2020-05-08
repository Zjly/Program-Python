from courses.computer_security.multiplicative_inverse import mul_inv


def same():
	x = 7
	y = 9
	mod = 11

	# 计算分母分子
	up = (3 * x ** 2 + 1) % mod
	down = (2 * y) % mod

	num_lambda = (up * mul_inv(down, mod)) % mod
	x3 = (num_lambda ** 2 - x - x) % 11
	y3 = ((x - x3) * num_lambda - y) % 11
	print("x3 =", x3, ", y3 =", y3)

def not_same():
	x1 = 7
	y1 = 9
	x2 = 2
	y2 = 4
	mod = 11

	# 计算分母分子
	up = (y2 - y1) % mod
	down = (x2 - x1) % mod

	num_lambda = (up * mul_inv(down, mod)) % mod
	x3 = (num_lambda ** 2 - x1 - x2) % 11
	y3 = ((x1 - x3) * num_lambda - y1) % 11
	print("x3 =", x3, ", y3 =", y3)

if __name__ == '__main__':
	same()
	not_same()
