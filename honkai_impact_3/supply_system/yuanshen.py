import random

ratio_5 = 0.006
ratio_4 = 0.051

time_4 = 0
time_5 = 0


def unit():
	global time_4
	global time_5

	# 抽取随机数
	random_number = random.random()

	# 保底计数
	time_4 = time_4 + 1
	time_5 = time_5 + 1

	# 5星保底
	if time_5 == 90:
		time_4 = 0
		time_5 = 0
		return 5

	# 4星保底
	if time_4 == 10:
		time_4 = 0

		# 5星概率
		ratio_time_5 = ratio_5 / (ratio_5 + ratio_4)

		# 保底出5星
		if 0 <= random_number < ratio_time_5:
			time_5 = 0
			return 5
		# 保底出4星
		else:
			return 4

	# 未保底 单抽出货
	if 0 <= random_number < ratio_4 + ratio_5:
		# 5星
		if 0 <= random_number < ratio_5:
			time_4 = 0
			time_5 = 0
			return 5
		# 4星
		elif ratio_5 <= random_number < ratio_5 + ratio_4:
			time_4 = 0
			return 4

	return 0


if __name__ == '__main__':
	times = 10000000
	get_5 = 0
	get_4 = 0
	for i in range(times):
		result = unit()
		if result == 5:
			get_5 += 1
		elif result == 4:
			get_4 += 1

	print(get_4 / times)
	print(get_5 / times)
	print((get_4 + get_5) / times)
