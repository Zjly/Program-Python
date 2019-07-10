# -*- coding:utf-8 -*-
import io
import sys
import urllib.parse
import chardet

import pandas as pd

# 读取敏感词库
lexicon = pd.read_csv("/var/www/test/python/lexicon.csv", sep=",", header=None)

def words_analysis(words):
	for sensitive_word in lexicon[1]:
		words = words.replace(sensitive_word, "*" * len(sensitive_word))
	return words


if __name__ == '__main__':
	data = sys.argv[1]
	result = words_analysis(data)
	print(result)
