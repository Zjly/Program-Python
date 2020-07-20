class Game:
	"""
	每一场比赛
	"""

	def __init__(self, team1, team2):
		"""
		初始化队伍
		"""
		self.team1 = team1
		self.team2 = team2

		self.father = None
		self.result1 = None
		self.result2 = None
		self.result3 = None
		self.result4 = None


class Result:
	"""
	每一种结果
	"""

	def __init__(self, team1, team2):
		"""
		初始化队伍
		"""
		self.team1 = team1
		self.team2 = team2

		self.score1 = None
		self.score2 = None
		self.win_team = None


def test():
	teams = ["AG", "QG", "ES", "TS", "WE", "ROX"]
	game_list = []
	for i in range(len(teams)):
		for j in range(i + 1, len(teams)):
			game = Game(teams[i], teams[j])
			game_list.append(game)

	print(len(game_list))


if __name__ == '__main__':
	test()
