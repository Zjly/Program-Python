def Max(array):
	if len(array) == 1:
		return array[0]
	else:
		left = Max(array[:len(array) // 2])
		right = Max(array[len(array) // 2:])
		if left > right:
			return left
		else:
			return right


if __name__ == '__main__':
	print(Max([3, 2, 5, 4, 1, 6]))
