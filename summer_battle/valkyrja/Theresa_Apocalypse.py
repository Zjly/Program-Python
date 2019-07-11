import random

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
		:return: 伤害值，伤害类型(物理/元素)，是否无视防御
		"""
		damage = random.randint(1, 16)
		return damage, "elemental", True, 4

	def attack_damage(self, attack_type):
		"""
		向敌人发出伤害
		:param attack_type: 攻击类型(普通/必杀)
		:return: 伤害值，伤害类型(物理/元素)，是否无视防御，攻击次数
		"""
		if attack_type == "ordinary":
			return self.attack, "physical", False, 1
		elif attack_type == "unique":
			return self.unique_skills()

	def defense_damage(self, damage, damage_type, ignore_defense, damage_count):
		"""
		受到敌人发出的伤害
		:param damage: 伤害值
		:param damage_type: 伤害类型(物理/元素)
		:param ignore_defense: 是否无视防御
		:param damage_count: 攻击次数
		:return:
		"""
		# 德丽莎被动受到元素伤害降低50%，故判定每次伤害，区分是否无视防御后，再进行元素伤害的减免计算
		for i in range(damage_count):
			if ignore_defense:
				if damage_type == "physical":
					self.health = self.health - damage
				elif damage_type == "elemental":
					self.health = self.health - damage * self.passive_skills()
			else:
				# 不知伤害减免是置于计算防御值之前还是之后，此处设置为先计算防御值
				damage_under_defense = damage - self.defense
				if damage_type == "physical":
					self.health = self.health - damage_under_defense
				elif damage_type == "elemental":
					self.health = self.health - damage_under_defense * self.passive_skills()
