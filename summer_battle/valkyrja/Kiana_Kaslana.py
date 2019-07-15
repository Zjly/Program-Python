from summer_battle.valkyrja.Damage import Damage
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
		damage = []
		for i in range(8):
			damage.append(12)
		return Damage(damage, "物理", False)

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
		# 琪亚娜无减免伤害的技能，且受到伤害与是否是元素伤害无关，故判定每次伤害，此时只需确定伤害类型是否无视防御即可
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