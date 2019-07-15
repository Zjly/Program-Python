import random
from datetime import datetime

from summer_battle.valkyrja.Kiana_Kaslana import KianaKaslana
from summer_battle.valkyrja.Theresa_Apocalypse import TheresaApocalypse


def begin_game(valKyrja1, valKyrja2):
	first_val, second_val = choose_gamer(valKyrja1, valKyrja2)

	game_round = 1
	while True:
		# print(f"Round {game_round}: ")
		# 先手玩家攻击
		damage_first_val = first_val.attack_damage(game_round)
		second_val.defense_damage(damage_first_val)
		if is_end(first_val, second_val) is not None:
			return is_end(first_val, second_val)

		# 后手玩家攻击
		damage_second_val = second_val.attack_damage(game_round)
		first_val.defense_damage(damage_second_val)
		if is_end(first_val, second_val) is not None:
			return is_end(first_val, second_val)

		game_round = game_round + 1

def choose_gamer(valKyrja1, valKyrja2):
	"""
	计算先手玩家
	:param valKyrja1: 女武神1
	:param valKyrja2: 女武神2
	:return: 先手玩家和后手玩家
	"""
	# 根据速度计算先手玩家，若速度相同则随机选择一名玩家先手
	if valKyrja1.speed > valKyrja2.speed:
		first_val = valKyrja1
		second_val = valKyrja2
	elif valKyrja1.speed < valKyrja2.speed:
		first_val = valKyrja2
		second_val = valKyrja1
	else:
		random_number = random.random()
		if random_number > 0.5:
			first_val = valKyrja1
			second_val = valKyrja2
		else:
			first_val = valKyrja2
			second_val = valKyrja1

	return first_val, second_val


def is_end(first_val, second_val):
	"""
	根据玩家血量判断游戏是否结束
	:param first_val:
	:param second_val:
	:return: 若结束返回胜者姓名，否则返回空
	"""
	if first_val.health <= 0:
		return second_val.name
	elif second_val.health <= 0:
		return first_val.name
	else:
		return None

def probabilistic_testing(game_count):
	valKyrja1_count = 0
	valKyrja2_count = 0
	begin_time = datetime.now()
	for i in range(game_count):
		kiana = KianaKaslana("琪亚娜", 100, 23, 11, 2)
		theresa = TheresaApocalypse("德丽莎", 100, 24, 8, 3)
		game_winner = begin_game(kiana, theresa)
		if game_winner == kiana.name:
			valKyrja1_count = valKyrja1_count + 1
		else:
			valKyrja2_count = valKyrja2_count + 1
	end_time = datetime.now()

	print(f"总场次: {game_count}, 计算耗时{end_time - begin_time}")
	print(f"琪亚娜胜场: {valKyrja1_count}, 胜率: {valKyrja1_count / game_count * 100}%")
	print(f"德丽莎胜场: {valKyrja2_count}, 胜率: {valKyrja2_count / game_count * 100}%")


if __name__ == '__main__':
	probabilistic_testing(1000000)
