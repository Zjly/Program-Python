import random

from honkai_impact_3.summer_battle.valkyrja.Damage import Damage
from honkai_impact_3.summer_battle.valkyrja.Valkyrja import ValKyrja


class YaeSakura(ValKyrja):
	"""
	八重樱
	"""

	def __init__(self, name, health, attack, defense, speed):
		super().__init__(name, health, attack, defense, speed)
		self.passive_skill = 0

	def passive_skills(self):
		"""
		被动技能：每次攻击有20%概率点燃敌人，每回合造成5点元素伤害，持续3回合，重复触发刷新持续时间
		:return:
		"""
		if random.random() > 0.2:
			return False
		else:
			return True

	def unique_skills(self):
		"""
		必杀技：每次攻击有25%概率造成的伤害（计算防御后）翻倍
		:return: 是否触发必杀技
		"""
		if random.random() > 0.25:
			return False
		else:
			return True

	def attack_damage(self, game_round):
		"""
		向敌人发出伤害
		:param game_round: 回合数
		:return: 攻击伤害，被动伤害，是否触发必杀
		"""
		# 是否重置被动
		if self.passive_skills():
			# print("八重樱触发了被动技能，", end="")
			self.passive_skill = 3

		# print(f"八重樱被动技能剩余回合数: {self.passive_skill}，", end="")

		# 是否发动必杀技
		if self.unique_skills():
			# print("八重樱触发了必杀技能，", end="")
			# 被动是否生效
			if self.passive_skill > 0:
				self.passive_skill = self.passive_skill - 1
				return Damage([self.attack], "物理", False), Damage([5], "元素", True), True
			else:
				return Damage([self.attack], "物理", False), Damage([0], "元素", True), True
		else:
			# 被动是否生效
			if self.passive_skill > 0:
				self.passive_skill = self.passive_skill - 1
				return Damage([self.attack], "物理", False), Damage([5], "元素", True), False
			else:
				return Damage([self.attack], "物理", False), Damage([0], "元素", True), False

	def defense_damage(self, damage):
		"""
		受到敌人发出的伤害
		:param damage: 伤害
		:return:
		"""
		# 八重樱无减免伤害的技能，且受到伤害与是否是元素伤害无关，故判定每次伤害，此时只需确定伤害类型是否无视防御即可
		for i in range(len(damage.value)):
			if damage.ignore:
				damage_final = damage.value[i]
			else:
				damage_final = damage.value[i] - self.defense
				if damage_final < 0:
					damage_final = 0
			self.health = self.health - damage_final
			# print(f"{self.name}受到{damage_final}点{damage.type}伤害，", end="")

		# print(f"{self.name}当前生命值为: {self.health}")
