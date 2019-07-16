import random
from datetime import datetime

from summer_battle.valkyrja.Fu_Hua import FuHua
from summer_battle.valkyrja.Yae_Sakura import YaeSakura


def begin_game(fu, sakura):
	game_round = 1
	while True:
		# print(f"Round {game_round}: ")
		# 符华攻击
		# print("符华发功了攻击：")
		damage_fu = fu.attack_damage(game_round)
		sakura.defense_damage(damage_fu)
		if is_end(fu, sakura) is not None:
			return is_end(fu, sakura)

		# print("八重樱发功了攻击：")
		# 八重樱攻击 普通攻击伤害 被动伤害 是否触发必杀技
		damage_sakura_normal, damage_sakura_passive, is_unique_skills = sakura.attack_damage(game_round)
		# 如若触发必杀技
		if is_unique_skills:
			fu.defense_damage(damage_sakura_normal)
			# 这里用两次攻击表示必杀技计算防御后的两倍伤害，如若第一次打出符华被动则不进行第二次攻击
			if not fu.passive_skill:
				fu.defense_damage(damage_sakura_normal)
		else:
			fu.defense_damage(damage_sakura_normal)

		# print("符华受到点燃伤害，", end="")
		fu.defense_damage(damage_sakura_passive)
		if is_end(fu, sakura) is not None:
			return is_end(fu, sakura)

		game_round = game_round + 1
		# print()


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
	fu_count = 0
	sakura_count = 0
	begin_time = datetime.now()
	for i in range(game_count):
		fu = FuHua("符华", 100, 27, 8, 9)
		sakura = YaeSakura("八重樱", 100, 28, 7, 8)
		game_winner = begin_game(fu, sakura)
		if game_winner == fu.name:
			fu_count = fu_count + 1
		else:
			sakura_count = sakura_count + 1
	end_time = datetime.now()

	print(f"总场次: {game_count}, 计算耗时{end_time - begin_time}")
	print(f"符华胜场: {fu_count}, 胜率: {fu_count / game_count * 100}%")
	print(f"八重樱胜场: {sakura_count}, 胜率: {sakura_count / game_count * 100}%")


if __name__ == '__main__':
	probabilistic_testing(1000000)
