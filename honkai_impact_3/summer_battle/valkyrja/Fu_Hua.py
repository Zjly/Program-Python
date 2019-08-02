import random

from honkai_impact_3.summer_battle.valkyrja.Damage import Damage
from honkai_impact_3.summer_battle.valkyrja.Valkyrja import ValKyrja


class FuHua(ValKyrja):
	"""
	符华
	"""

	def __init__(self, name, health, attack, defense, speed):
		super().__init__(name, health, attack, defense, speed)
		self.passive_skill = False

	def passive_skills(self):
		"""
		被动技能：首次受到致命伤害当回合不会死亡，生命值变为1并免疫元素伤害直到战斗结束
		:return:
		"""

	def unique_skills(self):
		"""
		必杀技：每3回合的一次攻击变为对敌人造成无视防御的10~30点元素伤害
		:return: 伤害值，伤害类型(物理/元素)，是否无视防御
		"""
		return Damage([random.randint(10, 30)], "元素", True)

	def attack_damage(self, game_round):
		"""
		向敌人发出伤害
		:param game_round: 回合数
		:return: 伤害值，伤害类型(物理/元素)，是否无视防御，攻击次数
		"""
		if game_round % 3 != 0:
			return Damage([self.attack], "物理", False)
		else:
			return self.unique_skills()

	def defense_damage(self, damage):
		"""
		受到敌人发出的伤害
		:param damage: 伤害
		:return:
		"""
		# 符华拥有被动技能
		for i in range(len(damage.value)):
			# 触发被动技能后免疫元素伤害
			if self.passive_skill == True and damage.type == "元素":
				# print("符华免疫了该次伤害", end="")
				return

			# 正常情况考虑
			if damage.ignore:
				damage_final = damage.value[i]
			else:
				damage_final = damage.value[i] - self.defense
				if damage_final < 0:
					damage_final = 0

			# 触发被动
			if self.health - damage_final <= 0 and self.passive_skill == False:
				self.passive_skill = True
				self.health = 1
				# print("符华触发了被动技能，", end="")
			else:
				self.health = self.health - damage_final
			# print(f"{self.name}受到{damage_final}点{damage.type}伤害，", end="")

		# print(f"{self.name}当前生命值为: {self.health}")
