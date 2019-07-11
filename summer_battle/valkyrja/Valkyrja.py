class ValKyrja:
	def __init__(self, name, health, attack, defense, speed):
		self.name = name
		self.health = health
		self.attack = attack
		self.defense = defense
		self.speed = speed

	def passive_skills(self):
		"""
		被动技能
		:return:
		"""
		pass

	def unique_skills(self):
		"""
		必杀技
		:return:
		"""
		pass

	def attack_damage(self, attack_type):
		"""
		向敌人发出伤害
		:return:
		"""
		pass

	def defense_damage(self, damage, damage_type, ignore_defense, damage_count):
		"""
		受到敌人发出的伤害
		:param damage: 伤害值
		:param damage_type: 伤害类型(物理/元素)
		:param ignore_defense: 是否无视防御
		:param damage_count: 攻击次数
		:return:
		"""
		pass