def fib1(n):
	if n == 1 or n == 2:
		return 1
	else:
		return fib1(n - 1) + fib1(n - 2)


def fib2(n):
	if n == 1 or n == 2:
		return 1
	else:
		pre1 = 1
		pre2 = 1
		this = 2
		for i in range(3, n + 1):
			this = pre1 + pre2
			pre1 = pre2
			pre2 = this

		return this


if __name__ == '__main__':
	for i in range(1, 10):
		print(fib1(i), end=" ")

	print()

	for i in range(1, 10):
		print(fib2(i), end=" ")
