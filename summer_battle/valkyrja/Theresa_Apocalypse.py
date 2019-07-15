import random
from time import sleep

from summer_battle.valkyrja.Damage import Damage
from summer_battle.valkyrja.Valkyrja import ValKyrja


class TheresaApocalypse(ValKyrja):
	"""
	德丽莎·阿波卡利斯
	"""

	def __init__(self, name, health, attack, defense, speed):
		super().__init__(name, health, attack, defense, speed)

	def passive_skills(self):
		"""
		被动技能：受到的元素伤害降低50%
		:return:
		"""
		return 0.5

	def unique_skills(self):
		"""
		必杀技：每2回合的一次攻击变为对敌人造成4次1~16点无视防御的元素伤害
		:return: 伤害
		"""
		damage = []
		for i in range(4):
			damage.append(random.randint(1, 16))
		return Damage(damage, "元素", True)

	def attack_damage(self, game_round):
		"""
		向敌人发出伤害
		:param game_round: 回合数
		:return: 伤害值，伤害类型(物理/元素)，是否无视防御，攻击次数
		"""
		if game_round % 2 != 0:
			return Damage([self.attack], "物理", False)
		else:
			return self.unique_skills()

	def defense_damage(self, damage):
		"""
		受到敌人发出的伤害
		:param damage: 伤害
		:return:
		"""
		# 德丽莎被动受到元素伤害降低50%，故判定每次伤害，区分是否无视防御后，再进行元素伤害的减免计算
		for i in range(len(damage.value)):
			if damage.ignore:
				if damage.type == "物理":
					damage_final = damage.value[i]
				else:
					damage_final = damage.value[i] * self.passive_skills()
			else:
				# 不知伤害减免是置于计算防御值之前还是之后，此处设置为先计算防御值
				damage_under_defense = damage.value[i] - self.defense
				if damage.type == "物理":
					damage_final = damage_under_defense
				else:
					damage_final = damage_under_defense * self.passive_skills()
			self.health = self.health - damage_final
			# print(f"{self.name}受到{damage_final}点{damage.type}伤害，", end="")

		# print(f"{self.name}当前生命值为: {self.health}")
