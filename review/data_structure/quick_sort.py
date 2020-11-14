def partition(array, i, j):
	temp = array[i]
	while i < j:
		while i < j and array[j] >= temp:
			j -= 1
		array[i] = array[j]
		while i < j and array[i] <= temp:
			i += 1
		array[j] = array[i]

	array[i] = temp
	return i


def quick_sort(array, s, t):
	if s < t:
		i = partition(array, s, t)
		quick_sort(array, s, i - 1)
		quick_sort(array, i + 1, t)


if __name__ == '__main__':
	array = [6, 8, 7, 9, 0, 1, 3, 2, 4, 5]

	quick_sort(array, 0, 9)

	print(array)
