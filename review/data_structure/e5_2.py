def Min(array, i):
	if i == 0:
		return array[0]
	else:
		min = Min(array, i - 1)
		if min > array[i]:
			return array[i]
		else:
			return min


if __name__ == '__main__':
	array = [3, 4, 6, 1, 3, 5, 8]
	print(Min(array, 6))
