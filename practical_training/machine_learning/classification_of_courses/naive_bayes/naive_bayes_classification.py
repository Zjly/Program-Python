from datetime import datetime
import pandas as pd
import jieba
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


def machine_learning(data):
	"""
	使用机器学习建立神经网络，对评论的倾向态度进行分析
	:param data:评论集(评论，倾向)
	:return:
	"""

	def chinese_word_cut(text):
		"""
		使用结巴分词对中文进行切分转化为独立的词语
		:param text: 完整的评论
		:return: 切分后的评论
		"""
		return " ".join(jieba.cut(text))

	# 进行分词并新建一列保存结果
	data["cut_name"] = data.name.apply(chinese_word_cut)

	# 确定评论部分(X)和标签部分(y)
	X = data["cut_name"]
	y = data["type"]

	# 设置随机数种子，这里要和进行预测时的随机数种子一样
	random_state = 42

	# 对数据集进行切分，分为训练集(train)和测试集(test)
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=random_state)

	def get_custom_stopwords(stop_words_file):
		"""
		得到停用词表
		:param stop_words_file:
		:return: 停用词表list
		"""
		with open(stop_words_file, encoding="utf-8") as f:
			stopwords = f.read()

		stopwords_list = stopwords.split("\n")
		custom_stopwords_list = [i for i in stopwords_list]
		return custom_stopwords_list

	# 得到停用词表，停用词是指在信息检索中，为节省存储空间和提高搜索效率，在处理自然语言数据之前或之后会自动过滤掉某些字或词
	stop_words_file = "./stop_words/哈工大停用词表.txt"
	stopwords = get_custom_stopwords(stop_words_file)

	# CountVectorizer是属于常见的特征数值计算类，是一个文本特征提取方法。对于每一个训练文本，它只考虑每种词汇在该训练文本中出现的频率
	# token_pattern：过滤规则，表示token的正则表达式，stop_words：设置停用词
	vect = CountVectorizer(token_pattern=u'(?u)\\b\\w+\\b', stop_words=frozenset(stopwords))

	nb = MultinomialNB()

	X_train_vect = vect.fit_transform(X_train)
	nb.fit(X_train_vect, y_train)
	train_score = nb.score(X_train_vect, y_train)
	print(train_score)

	X_test_vect = vect.transform(X_test)
	print(nb.score(X_test_vect, y_test))


if __name__ == '__main__':
	comments_data = pd.read_csv("courses.csv")

	start_time = datetime.now()
	machine_learning(comments_data)
	end_time = datetime.now()
	print("total time: " + str(end_time - start_time))
