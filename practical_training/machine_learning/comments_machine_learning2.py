import os
from datetime import datetime

import numpy as np
import pandas as pd
import tflearn
from sklearn import preprocessing
from snownlp import SnowNLP
import jieba
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from tflearn.data_utils import to_categorical, pad_sequences


def snow_test(data):
	def snow_result(comment):
		s = SnowNLP(comment)
		if s.sentiments >= 0.5:
			return 1
		else:
			return 0

	data['snlp_result'] = data.comment.apply(snow_result)

	counts = 0
	for i in range(len(data)):
		if data.iloc[i, 1] == data.iloc[i, 2]:
			counts += 1
	print("准确率: " + str(counts / len(data)))


def machine_learning1(data):
	def chinese_word_cut(text):
		return " ".join(jieba.cut(text))

	data["cut_comment"] = data.comment.apply(chinese_word_cut)

	X = data["cut_comment"]
	y = data["evaluation"]

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

	def get_custom_stopwords(stop_words_file):
		with open(stop_words_file, encoding="utf-8") as f:
			stopwords = f.read()

		stopwords_list = stopwords.split("\n")
		custom_stopwords_list = [i for i in stopwords_list]
		return custom_stopwords_list

	stop_words_file = "./stop_words/哈工大停用词表.txt"
	stopwords = get_custom_stopwords(stop_words_file)

	vect = CountVectorizer(max_df=0.8, min_df=3, token_pattern=u'(?u)\\b[^\\d\\W]\\w+\\b',
						   stop_words=frozenset(stopwords))

	test = pd.DataFrame(vect.fit_transform(X_train).toarray(), columns=vect.get_feature_names())

	nb = MultinomialNB()
	X_train_vect = vect.fit_transform(X_train)
	nb.fit(X_train_vect, y_train)
	train_score = nb.score(X_train_vect, y_train)
	print(train_score)

	X_test_vect = vect.transform(X_test)
	print(nb.score(X_test_vect, y_test))

	X_vec = vect.transform(X)
	nb_result = nb.predict(X_vec)
	data['nb_result'] = nb_result

	print(data)

def machine_learning2(data):
	def chinese_word_cut(text):
		return " ".join(jieba.cut(text))

	data["cut_comment"] = data.comment.apply(chinese_word_cut)

	X = data["cut_comment"]
	y = data["evaluation"]

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

	def get_custom_stopwords(stop_words_file):
		with open(stop_words_file, encoding="utf-8") as f:
			stopwords = f.read()

		stopwords_list = stopwords.split("\n")
		custom_stopwords_list = [i for i in stopwords_list]
		return custom_stopwords_list

	stop_words_file = "./stop_words/哈工大停用词表.txt"
	stopwords = get_custom_stopwords(stop_words_file)

	vect = CountVectorizer(max_df=0.8, min_df=3, token_pattern=u'(?u)\\b[^\\d\\W]\\w+\\b',
						   stop_words=frozenset(stopwords))

	vect.fit(X_train)
	vocab = vect.vocabulary_

	def convert_X_to_X_word_ids(X):
		return X.apply(lambda x: [vocab[w] for w in [w.lower().strip() for w in x.split()] if w in vocab])

	X_train_word_ids = convert_X_to_X_word_ids(X_train)
	X_test_word_ids = convert_X_to_X_word_ids(X_test)

	# 序列扩充
	X_test_padded_seqs = pad_sequences(X_test_word_ids, maxlen=20, value=0)
	X_train_padded_seqs = pad_sequences(X_train_word_ids, maxlen=20, value=0)

	# 标签集处理
	unique_y_labels = list(y_train.value_counts().index)
	le = preprocessing.LabelEncoder()
	le.fit(unique_y_labels)

	y_train = to_categorical(y_train.map(lambda x: le.transform([x])[0]), nb_classes=len(unique_y_labels))
	y_test = to_categorical(y_test.map(lambda x: le.transform([x])[0]), nb_classes=len(unique_y_labels))

	# 构造网络
	n_epoch = 100
	size_of_each_vector = X_train_padded_seqs.shape[1]
	vocab_size = len(vocab)
	no_of_unique_y_labels = len(unique_y_labels)

	net = tflearn.input_data(
		[None, size_of_each_vector])  # The first element is the "batch size" which we set to "None"
	net = tflearn.embedding(net, input_dim=vocab_size, output_dim=128)  # input_dim: vocabulary size
	net = tflearn.lstm(net, 128, dropout=0.6)  # Set the dropout to 0.6
	net = tflearn.fully_connected(net, no_of_unique_y_labels, activation='softmax')  # relu or softmax
	net = tflearn.regression(net, optimizer='adam', learning_rate=1e-4, loss='categorical_crossentropy')

	# 训练网络

	# 初始化
	model = tflearn.DNN(net, tensorboard_verbose=0, tensorboard_dir="./tflearn_data/tflearn_logs/")

	# 训练
	model.fit(X_train_padded_seqs, y_train, validation_set=(X_test_padded_seqs, y_test), n_epoch=n_epoch,
			  show_metric=True, batch_size=100)

	# 保存
	time = datetime.now()
	time_str = str(time).replace(":", ".")
	os.makedirs(f"./tflearn_data/tflearn_modes/{time_str}")
	model.save(f"./tflearn_data/tflearn_modes/{time_str}/comment_mode.tflearn")

if __name__ == '__main__':
	comments_data = pd.read_csv("comments.csv")
	# snow_test(comments_data)
	# machine_learning1(comments_data)
	machine_learning2(comments_data)
