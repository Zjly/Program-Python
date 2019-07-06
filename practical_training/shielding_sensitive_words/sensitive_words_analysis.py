from datetime import time, datetime

import pandas as pd

# 读取敏感词库
lexicon = pd.read_csv("lexicon.csv", sep=",", header=None)


def words_analysis(words):
	for sensitive_word in lexicon[1]:
		words = words.replace(sensitive_word, "*" * len(sensitive_word))
	return words


if __name__ == '__main__':
	start_time = datetime.now()
	print(words_analysis("这门课考试作弊很简单；法轮功是邪教"))
	end_time = datetime.now()
	print(end_time - start_time)
