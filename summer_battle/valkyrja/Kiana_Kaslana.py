from summer_battle.valkyrja.Valkyrja import ValKyrja


class KianaKaslana(ValKyrja):
	"""
	琪亚娜·卡斯兰娜
	"""
	def __init__(self, name, health, attack, defense, speed):
		super().__init__(name, health, attack, defense, speed)
		self.passive_skills()

	def passive_skills(self):
		"""
		被动技能：生命值上限提高20点
		:return:
		"""
		self.health = self.health + 20

	def unique_skills(self):
		"""
		必杀技：每3回合的一次攻击变为对敌人进行8次攻击，每次造成12点伤害
		:return: 伤害值，伤害类型(物理/元素)，是否无视防御，攻击次数
		"""
		return 12, "physical", False, 8

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
		# 琪亚娜无减免伤害的技能，且受到伤害与是否是元素伤害无关，故判定每次伤害，此时只需确定伤害类型是否无视防御即可
		for i in range(damage_count):
			if ignore_defense:
				self.health = self.health - damage
			else:
				damage_under_defense = damage - self.defense
				if damage_under_defense > 0:
					self.health = self.health - damage_under_defense