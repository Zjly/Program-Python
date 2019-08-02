# 计算得出单抽非保底4星出货率为4.875%

import random

# 分别为武器官方出货率、圣痕官方出货率、总出货率（都包括十连保底）
ratio_of_weapon = 0.04958
ratio_of_holy_scar = 0.07437
ratio_of_all = ratio_of_weapon + ratio_of_holy_scar

def get_ratio_of_star4(ratio_of_per):
	"""
	得到当前预测出货率下的实际出货率
	:param ratio_of_per: 预测出货率
	:return: 实际出货率
	"""
	# 测试次数
	count = 10000000

	count_of_all = 0
	num_in_ten = 0

	# 通过预测出货率与随机数的比较计算该次抽卡是否出货
	for i in range(count):
		random_number = random.random()

		if random_number < ratio_of_per:
			count_of_all += 1
			num_in_ten = 0
			continue
		else:
			num_in_ten += 1

		# 计算十连保底
		if num_in_ten == 10:
			count_of_all += 1
			num_in_ten = 0

	return count_of_all / count

def calculate_ratio():
	"""
	计算出货率
	:return:
	"""
	# 测试数据范围和学习速率
	ratio_begin = 0.0485
	learn_rate = 0.0001
	ratio_end = 0.049

	ratio = ratio_begin
	while ratio < ratio_end:
		ratio_of_per = get_ratio_of_star4(ratio)
		print(f"测试概率: {ratio}, 预测出货率: {ratio_of_all}, 实际出货率: {ratio_of_per}")
		ratio += learn_rate


if __name__ == '__main__':
	calculate_ratio()