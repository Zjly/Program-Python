import numpy as np
import pandas as pd

# 读取敏感词库
lexicon = pd.read_csv("lexicon.csv", sep=",", header=None)

def words_analysis(words):
	for sensitive_word in lexicon[1]:
		words = words.replace(sensitive_word, "***")
	return words


if __name__ == '__main__':
	print(words_analysis(""))