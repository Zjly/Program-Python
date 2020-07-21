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

		self.result_list = []


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
		self.next_game = None

	def __str__(self):
		return self.team1 + " " + str(self.score1) + ":" + str(self.score2) + " " + self.team2


def get_game_list():
	"""
	得到游戏比赛列表
	:return:
	"""
	# teams = ["AG", "QG", "ES", "TS", "WE", "ROX"]
	teams = ["AG", "QG", "ES"]
	scores = [2, 2, 1, 0]
	game_list = []

	for i in range(len(teams)):
		for j in range(i + 1, len(teams)):
			# 创建game
			game = Game(teams[i], teams[j])
			# 创建结果
			for k in range(4):
				# 设置result
				result = Result(teams[i], teams[j])
				result.score1 = scores[k]
				result.score2 = scores[3 - k]
				if k < 2:
					result.win_team = teams[i]
				else:
					result.win_team = teams[j]

				game.result_list.append(result)

			game_list.append(game)

	return game_list


def get_game_tree(game_list):
	"""
	得到游戏树
	:param game_list:
	:return:
	"""
	for i in range(len(game_list) - 1):
		game = game_list[i]
		game_next = game_list[i + 1]
		for j in range(4):
			game.result_list[j].next_game = game_next

	return game_list


def traverse_tree(game, game_result, game_result_list):
	"""
	遍历树 完成各种可能性列表的建立
	:param game:
	:param game_result:
	:param game_result_list:
	:return:
	"""
	# 对当前game的每一种情况进行循环考虑
	for i in range(4):
		# 新建一条比赛结果分支 并拉取之前比赛结果分支 使用game_result[:]进行副本的传递而不是源文件
		current_game_result = game_result[:]
		# 将当前game的当前情况加入到分支当中
		current_game_result.append(game.result_list[i])
		# 递归继续下一个game
		if game.result_list[i].next_game is not None:
			traverse_tree(game.result_list[i].next_game, current_game_result, game_result_list)
		# 如若结束 将比赛结果分支加入到列表当中
		else:
			game_result_list.append(current_game_result)

	return game_result_list

def printGR(game_result_list):
	"""
	结果输出
	:param game_result_list:
	:return:
	"""
	for i in range(len(game_result_list)):
		game_result = game_result_list[i]
		game_str = str(i)
		game_str += "	:	"
		for j in range(len(game_result)):
			result = game_result[j]
			game_str += result.team1 + " " + str(result.score1) + ":" + str(result.score2) + " " + result.team2
			game_str += "    "
		print(game_str)
	pass

if __name__ == '__main__':
	g_list = get_game_list()
	g_list = get_game_tree(g_list)
	g_r_list = traverse_tree(g_list[0], [], [])
	printGR(g_r_list)
	pass
