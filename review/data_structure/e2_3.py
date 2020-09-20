def e2_3(array, x):
	j = 0
	for i in range(len(array)):
		if array[i] != x:
			array[j] = array[i]
			j = j + 1


if __name__ == '__main__':
	array = [1, 2, 3, 2, 3, 1]
	e2_3(array, 3)
	print(array)