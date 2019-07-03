from snownlp import SnowNLP

text = "老师给分有点差"
s = SnowNLP(text)

for sentence in s.sentences:
	print(sentence)

print("这句话代表正面情感的概率: " + str(s.sentiments * 100) + "%")