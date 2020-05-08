from courses.computer_security.multiplicative_inverse import mul_inv


def same():
	x = 3
	y = 2
	mod = 19

	# 计算分母分子
	up = (3 * x ** 2 + 8) % mod
	down = (2 * y) % mod

	num_lambda = (up * mul_inv(down, mod)) % mod
	x3 = (num_lambda ** 2 - x - x) % mod
	y3 = ((x - x3) * num_lambda - y) % mod
	print("x3 =", x3, ", y3 =", y3)

def not_same():
	x1 = 10
	y1 = 8
	x2 = 3
	y2 = 2
	mod = 19

	# 计算分母分子
	up = (y2 - y1) % mod
	down = (x2 - x1) % mod

	num_lambda = (up * mul_inv(down, mod)) % mod
	x3 = (num_lambda ** 2 - x1 - x2) % mod
	y3 = ((x1 - x3) * num_lambda - y1) % mod
	print("x3 =", x3, ", y3 =", y3)

if __name__ == '__main__':
	same()
	not_same()
