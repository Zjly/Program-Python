# -*- coding:utf-8 -*-
import io
import sys
import urllib.parse

import jieba
import tflearn
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from tflearn.data_utils import pad_sequences


def comment_predict(data):
	"""
	根据已有模型对评论倾向进行预测
	:return:
	"""
	# 建立模型时用到的评论数据
	predict_data = pd.read_csv("/var/www/test/python/comments_tag.csv")

	def chinese_word_cut(text):
		"""
		使用结巴分词对中文进行切分转化为独立的词语
		:param text: 完整的评论
		:return: 切分后的评论
		"""
		return " ".join(jieba.cut(text))

	# 进行分词并新建一列保存结果
	predict_data["cut_comment"] = predict_data.comment.apply(chinese_word_cut)

	# 确定评论部分(X)和标签部分(y)
	X = predict_data["cut_comment"]
	y = predict_data["evaluation"]

	# 对数据集进行切分，分为训练集(train)和测试集(test)
	# 这里随机数种子要和建立模型时的随机数种子一样
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

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

	# 得到停用词表
	stop_words_file = "/var/www/test/python/哈工大停用词表.txt"
	stopwords = get_custom_stopwords(stop_words_file)

	# 计算特征数值
	vect = CountVectorizer(max_df=0.8, min_df=3, token_pattern=u'(?u)\\b\\w+\\b', stop_words=frozenset(stopwords))
	vect.fit(X_train)
	vocab = vect.vocabulary_

	def convert_X_to_X_word_ids(X):
		"""
		将评论(文字部分)转化为id集(数值序列)
		:param X:评论集合
		:return:数值序列
		"""
		return X.apply(lambda x: [vocab[w] for w in [w.lower().strip() for w in x.split()] if w in vocab])

	# 序列扩充，统一延长到长度为20的序列，使得评论序列格式相同，不足的用0代替
	X_train_word_ids = convert_X_to_X_word_ids(X_train)
	X_train_padded_seqs = pad_sequences(X_train_word_ids, maxlen=20, value=0)

	# 标签集处理
	unique_y_labels = list(y_train.value_counts().index)
	le = preprocessing.LabelEncoder()
	le.fit(unique_y_labels)

	# 构造网络
	size_of_each_vector = X_train_padded_seqs.shape[1]
	vocab_size = len(vocab)
	no_of_unique_y_labels = len(unique_y_labels)

	net = tflearn.input_data([None, size_of_each_vector])
	net = tflearn.embedding(net, input_dim=vocab_size, output_dim=128)
	net = tflearn.lstm(net, 128, dropout=0.6)
	net = tflearn.fully_connected(net, no_of_unique_y_labels, activation='softmax')
	net = tflearn.regression(net, optimizer='adam', learning_rate=1e-4, loss='categorical_crossentropy')

	# 初始化
	model = tflearn.DNN(net, tensorboard_verbose=0)

	# 加载模型
	model.load("/var/www/test/python/2019-07-10 20.03.06.175272(1000, 42)/model")

	# ———————————————————————————————————————预测部分———————————————————————————————————————
	# 待预测的评论数据
	predict_data = data

	# 对评论数据进行分词
	predict_data["cut_comment"] = predict_data.comment.apply(chinese_word_cut)

	# 设置预测集
	predict_X = predict_data["cut_comment"]

	# 转化为数值序列
	predict_X_word_ids = convert_X_to_X_word_ids(predict_X)
	predict_X_padded_seqs = pad_sequences(predict_X_word_ids, maxlen=20, value=0)

	# 进行预测并得到结果
	predict_Y = model.predict(predict_X_padded_seqs)

	# 输出结果
	get_evaluation(predict_Y)


def get_evaluation(predict_Y):
	"""
	根据结果ndarray得到评论的倾向
	:param predict_Y:
	:return:
	"""
	for evaluation in predict_Y:
		# 得到good的值
		good = evaluation[1]

		# 设置一个阈值，这里定为0.5，大于阈值则说明该评论倾向于good
		if good > 0.5:
			print("good: " + str(round(good * 100, 2)) + "%")
		else:
			print("bad: " + str(round(good * 100, 2)) + "%")


if __name__ == '__main__':
	comment = sys.argv[1]
	data = pd.DataFrame({'comment': comment}, index=[0])
	comment_predict(data)
