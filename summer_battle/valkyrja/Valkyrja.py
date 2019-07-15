class ValKyrja:
	def __init__(self, name, health, attack, defense, speed):
		"""
		初始化女武神信息
		:param name: 女武神姓名
		:param health: 女武神生命值
		:param attack: 女武神攻击
		:param defense: 女武神防御
		:param speed: 女武神速度：极慢(1)，慢(2)，较慢(3)，一般(5)，较快(7)，快(8)，极快(9)
		"""
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

	def attack_damage(self, game_round):
		"""
		向敌人发出伤害
		:param game_round: 游戏回合
		:return:
		"""
		pass

	def defense_damage(self, damage):
		"""
		受到敌人发出的伤害
		:param damage: 伤害类对象
		:return:
		"""
		pass