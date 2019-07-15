class Damage:
	def __init__(self, value, type, ignore):
		"""
		初始化伤害信息
		:param value: 伤害值
		:param type: 伤害类型(物理/元素)
		:param ignore: 是否无视防御
		"""
		self.value = value
		self.type = type
		self.ignore = ignore
