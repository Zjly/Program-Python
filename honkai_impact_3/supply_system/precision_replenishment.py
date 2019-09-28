# 通过测试后发现，毕业装备需要平均152.07抽；如若算上二换一，毕业装备需要120.92抽

import random

# 分别为单抽非保底出货率、武器出货率和圣痕出货率
ratio_of_per = 0.04875
ratio_of_weapon = 0.0195
ratio_of_holy_scar = 0.02925

# 根据官方所给数据计算出up比例占其中的50%
ratio_of_weapon_up = ratio_of_weapon * 0.5
ratio_of_holy_scar_up = ratio_of_holy_scar * 0.5
ratio_of_holy_scar_up_per = ratio_of_holy_scar_up / 3

# 十连保底计数
num_in_ten = 0


def get_equipment():
	"""
	抽取装备
	:return:
	"""
	global num_in_ten
	random_number = random.random()

	# 计算是否出货，后面的分支均为判断出的是什么
	if random_number < ratio_of_weapon + ratio_of_holy_scar:
		num_in_ten = 0

		if 0 < random_number < ratio_of_weapon_up:
			return "up武器"
		elif ratio_of_weapon_up < random_number < ratio_of_weapon:
			return "非up武器"
		elif ratio_of_weapon < random_number < ratio_of_weapon + ratio_of_holy_scar_up_per:
			return "up圣痕（上）"
		elif ratio_of_weapon + ratio_of_holy_scar_up_per < random_number < ratio_of_weapon + ratio_of_holy_scar_up_per * 2:
			return "up圣痕（中）"
		elif ratio_of_weapon + ratio_of_holy_scar_up_per * 2 < random_number < ratio_of_weapon + ratio_of_holy_scar_up:
			return "up圣痕（下）"
		elif ratio_of_weapon + ratio_of_holy_scar_up < random_number < ratio_of_weapon + ratio_of_holy_scar:
			return "非up圣痕"
	else:
		num_in_ten += 1

		# 非出货时计算是否是十连保底
		if num_in_ten == 10:
			num_in_ten = 0
			random_number = random.random()
			if random_number < 0.2:
				return "up武器"
			elif random_number < 0.4:
				return "非up武器"
			elif random_number < 0.5:
				return "up圣痕（上）"
			elif random_number < 0.6:
				return "up圣痕（中）"
			elif random_number < 0.7:
				return "up圣痕（下）"
			else:
				return "非up圣痕"
		else:
			return "啥都没出"


def get_num_of_graduation1():
	"""
	得到毕业装备的抽取数，不计算许愿
	:return: 毕业装备的抽取数
	"""
	weapon = False
	holy_scar1 = False
	holy_scar2 = False
	holy_scar3 = False

	count = 0
	# 只要毕业即停止循环
	while not (weapon and holy_scar1 and holy_scar2 and holy_scar3):
		count += 1
		result = get_equipment()
		if result == "up武器":
			weapon = True
		elif result == "up圣痕（上）":
			holy_scar1 = True
		elif result == "up圣痕（中）":
			holy_scar2 = True
		elif result == "up圣痕（下）":
			holy_scar3 = True

	return count


def get_num_of_graduation2():
	"""
	得到毕业装备的抽取数，计算许愿
	:return: 毕业装备的抽取数
	"""
	weapon = 0
	holy_scar1 = 0
	holy_scar2 = 0
	holy_scar3 = 0

	count = 0

	# 算上2换1的情况，进行各种条件的判断
	while not (weapon >= 1 and ((holy_scar1 >= 1 and holy_scar2 >= 1 and holy_scar3 >= 1) or (
			holy_scar1 + holy_scar2 + holy_scar3 >= 4 and (
			(holy_scar1 >= 1 and holy_scar2 >= 1) or (holy_scar1 >= 1 and holy_scar3 >= 1) or (
			holy_scar2 >= 1 and holy_scar3 >= 1))))):
		count += 1
		result = get_equipment()
		if result == "up武器":
			weapon += 1
		elif result == "up圣痕（上）":
			holy_scar1 += 1
		elif result == "up圣痕（中）":
			holy_scar2 += 1
		elif result == "up圣痕（下）":
			holy_scar3 += 1

	return count


def get_num_of_graduation3():
	"""
	得到毕业装备的抽取数，计算武器保底
	:return: 毕业装备的抽取数
	"""
	global num_in_ten

	weapon = 0
	holy_scar1 = 0
	holy_scar2 = 0
	holy_scar3 = 0

	count = 0

	# 算上2换1的情况，进行各种条件的判断
	while not (weapon >= 1 and ((holy_scar1 >= 1 and holy_scar2 >= 1 and holy_scar3 >= 1) or (
			holy_scar1 + holy_scar2 + holy_scar3 >= 4 and (
			(holy_scar1 >= 1 and holy_scar2 >= 1) or (holy_scar1 >= 1 and holy_scar3 >= 1) or (
			holy_scar2 >= 1 and holy_scar3 >= 1))))):
		count += 1

		if count == 60 and weapon == 0:
			weapon += 1
			num_in_ten = 0
			continue

		result = get_equipment()
		if result == "up武器":
			weapon += 1
		elif result == "up圣痕（上）":
			holy_scar1 += 1
		elif result == "up圣痕（中）":
			holy_scar2 += 1
		elif result == "up圣痕（下）":
			holy_scar3 += 1

	return count


def get_avg_count():
	"""
	计算平均出货的次数
	:return:
	"""
	num = 100000
	sum_of_count = 0
	for i in range(num):
		count = get_num_of_graduation3()
		sum_of_count += count
	# print(f"{i}: 毕业所需{count}抽")

	print(f"测试次数: {num}, 平均毕业套所需{sum_of_count / num}次抽取！")


if __name__ == '__main__':
	get_avg_count()
