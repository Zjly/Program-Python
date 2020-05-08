def mul_inv(num, mod):
	# 初始化
	Q = 0
	X1 = 1
	X2 = 0
	X3 = mod
	Y1 = 0
	Y2 = 1
	Y3 = num
	result = 0
	print("Q	X1	X2	X3	Y1	Y2	Y3")
	print(Q, X1, X2, X3, Y1, Y2, Y3, sep="	")

	while Y3 != 1:
		Q = X3 // Y3

		P1 = Y1
		P2 = Y2
		P3 = Y3

		Y1 = X1 - Y1 * Q
		Y2 = X2 - Y2 * Q
		Y3 = X3 - Y3 * Q

		X1 = P1
		X2 = P2
		X3 = P3

		print(Q, X1, X2, X3, Y1, Y2, Y3, sep="	")

		result = Y2
		if Y2 < 0:
			result = mod + Y2

	return result


if __name__ == '__main__':
	mul_inv(7, 11)
