import pandas as pd


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
		self.loss_team = None
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
					result.loss_team = teams[j]
				else:
					result.win_team = teams[j]
					result.loss_team = teams[i]

				game.result_list.append(result)

			game_list.append(game)

	return game_list


def get_game(team1, team2):
	"""
	创建两个队的比赛
	:param team1:
	:param team2:
	:return:
	"""
	scores = [2, 2, 1, 0]

	# 创建game
	game = Game(team1, team2)
	# 创建结果
	for k in range(4):
		# 设置result
		result = Result(team1, team2)
		result.score1 = scores[k]
		result.score2 = scores[3 - k]
		if k < 2:
			result.win_team = team1
			result.loss_team = team2
		else:
			result.win_team = team2
			result.loss_team = team1

		game.result_list.append(result)

	return game


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


def calculate_score(game_result_list):
	"""
	计算分数
	:param game_result_list:
	:return:
	"""
	# teams = ["AG", "QG", "ES"]
	teams = ["AG", "QG", "ES", "WE", "TS"]
	game_score_list = []
	for game_result in game_result_list:
		# 建立并初始化DataFrame
		score = pd.DataFrame(index=teams, columns=["win", "loss", "diff", "score"])
		score.loc[:, :] = 0

		# 导入比赛数据
		for result in game_result:
			score.loc[result.win_team, "win"] += 1
			score.loc[result.loss_team, "loss"] += 1
			score.loc[result.win_team, "score"] += 1

			current_diff = result.score1 - result.score2
			score.loc[result.win_team, "diff"] += abs(current_diff)
			score.loc[result.loss_team, "diff"] += -abs(current_diff)

		# 排序
		score = score.sort_values(by=["score", "diff"], ascending=False)
		game_score_list.append([game_result, score])

	return game_score_list


def printGSL(game_score_list):
	"""
	结果输出
	:param game_score_list:
	:return:
	"""
	for i in range(len(game_score_list)):
		game_result = game_score_list[i][0]
		game_score = game_score_list[i][1]

		# 输出比分
		game_str = str(i)
		game_str += "	:	"
		for j in range(len(game_result)):
			result = game_result[j]
			game_str += result.team1 + " " + str(result.score1) + ":" + str(result.score2) + " " + result.team2
			game_str += "    "
		print(game_str)

		# 输出分数
		print(game_score)
		print("---------------------------------")


def test():
	"""
	测试程序是否成功
	:return:
	"""
	g_list = get_game_list()
	g_list = get_game_tree(g_list)
	g_r_list = traverse_tree(g_list[0], [], [])
	g_s_list = calculate_score(g_r_list)
	printGSL(g_s_list)


def create_game_list():
	"""
	创建比赛列表
	:return:
	"""
	game_list = []
	game1 = get_game("TS", "WE")
	game2 = get_game("AG", "WE")
	game3 = get_game("TS", "QG")
	game4 = get_game("AG", "ES")
	game_list.append(game1)
	game_list.append(game2)
	game_list.append(game3)
	game_list.append(game4)
	return game_list


def add_exist_result(game_score_list):
	"""
	手动加入已完比赛比分
	:param game_score_list:
	:return:
	"""
	for i in range(len(game_score_list)):
		game_score = game_score_list[i][1]

		game_score.loc["TS", "win"] += 2
		game_score.loc["TS", "loss"] += 1
		game_score.loc["TS", "diff"] += 2
		game_score.loc["TS", "score"] = game_score.loc["TS", "win"]

		game_score.loc["WE", "win"] += 2
		game_score.loc["WE", "loss"] += 1
		game_score.loc["WE", "diff"] += 2
		game_score.loc["WE", "score"] = game_score.loc["WE", "win"]

		game_score.loc["QG", "win"] += 2 + 1
		game_score.loc["QG", "loss"] += 1
		game_score.loc["QG", "diff"] += 2 + 2
		game_score.loc["QG", "score"] = game_score.loc["QG", "win"]

		game_score.loc["ES", "win"] += 2 + 1
		game_score.loc["ES", "loss"] += 1
		game_score.loc["ES", "diff"] += 1 + 2
		game_score.loc["ES", "score"] = game_score.loc["ES", "win"]

		game_score.loc["AG", "win"] += 0 + 1
		game_score.loc["AG", "loss"] += 2
		game_score.loc["AG", "diff"] += -3 + 2
		game_score.loc["AG", "score"] = game_score.loc["AG", "win"]

		# 排序
		game_score_list[i][1] = game_score.sort_values(by=["score", "diff"], ascending=False)


def run():
	"""
	运行程序
	:return:
	"""
	g_list = create_game_list()
	g_list = get_game_tree(g_list)
	g_r_list = traverse_tree(g_list[0], [], [])
	g_s_list = calculate_score(g_r_list)
	add_exist_result(g_s_list)
	printGSL(g_s_list)


if __name__ == '__main__':
	# test()
	run()
