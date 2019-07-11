import random

from summer_battle.valkyrja.Kiana_Kaslana import KianaKaslana
from summer_battle.valkyrja.Theresa_Apocalypse import TheresaApocalypse

def begin_game(valKyrja1, valKyrja2):
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


	round = 1
	while first_val.health > 0 or second_val.health > 0:
		# TODO 回合攻击流程编写
		# 先手玩家攻击
		damage_first_val = first_val.attack_damage()

if __name__ == '__main__':
	kiana = KianaKaslana("琪亚娜", 100, 23, 11, 2)
	theresa = TheresaApocalypse("德丽莎", 100, 24, 8, 3)
	begin_game(kiana, theresa)