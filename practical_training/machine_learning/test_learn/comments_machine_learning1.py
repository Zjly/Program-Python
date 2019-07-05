import os
from datetime import datetime

import numpy as np
import pandas as pd
import pymysql
import tflearn

import tensorflow
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from tflearn.data_utils import pad_sequences, to_categorical, VocabularyProcessor
from sklearn import preprocessing


def get_comment_from_database():
	"""
	从数据库中得到评论
	:return: 评论的DataFramework
	"""
	conn = pymysql.connect("localhost", "root", "root", "test")
	comments = pd.read_sql(sql="select comment_content, comment_quality from cm_comment", con=conn)
	comments.columns = ["content", "quality"]
	return comments


def machine_learning(comments):
	# 划分样本集和标签集
	X = comments["content"]
	y = comments["quality"]

	# 分类训练集和测试集
	random_state = 42
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=random_state)

	# 将样本集的字符串转变为数字序列。创建vocab，把X转化为X_word_ids
	vect = CountVectorizer(ngram_range=(1, 1), token_pattern=r'\b\w{1,}\b')
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
	n_epoch = 10
	size_of_each_vector = X_train_padded_seqs.shape[1]
	vocab_size = len(vocab)
	no_of_unique_y_labels = len(unique_y_labels)

	net = tflearn.input_data([None, size_of_each_vector])
	net = tflearn.embedding(net, input_dim=vocab_size, output_dim=128)
	net = tflearn.lstm(net, 128, dropout=0.6)
	net = tflearn.fully_connected(net, no_of_unique_y_labels, activation='softmax')
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
	os.makedirs(f"./tflearn_data/tflearn_models/{time_str}({n_epoch}, {random_state})")
	model.save(f"./tflearn_data/tflearn_models/{time_str}({n_epoch}, {random_state})/model")


if __name__ == '__main__':
	comments_list = get_comment_from_database()

	start_time = datetime.now()
	machine_learning(comments_list)
	end_time = datetime.now()
	print("total time: " + str(end_time - start_time))
