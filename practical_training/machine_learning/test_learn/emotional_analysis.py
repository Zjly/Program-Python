from snownlp import SnowNLP

text = "cnm"
s = SnowNLP(text)

for sentence in s.sentences:
	print(sentence)

print("这句话代表正面情感的概率: " + str(s.sentiments * 100) + "%")