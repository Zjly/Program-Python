import io
import sys
import urllib.parse

import pandas as pd

# 读取敏感词库
lexicon = pd.read_csv("E:\Coding\Python\Program\practical_training\connect_php\lexicon.csv", sep=",", header=None)


def words_analysis(words):
	for sensitive_word in lexicon[1]:
		words = words.replace(sensitive_word, "*" * len(sensitive_word))
	return words


if __name__ == '__main__':
	sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
	data = urllib.parse.unquote(sys.argv[1])
	result = words_analysis(data)
	print(result)

