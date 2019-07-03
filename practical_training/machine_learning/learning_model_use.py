import os
from datetime import datetime

import pandas as pd
import pymysql
import tflearn

import tensorflow
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from tflearn.data_utils import pad_sequences, to_categorical
from sklearn import preprocessing

# TODO 数字序列几乎都是0 该问题亟待解决
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
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

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

	# 初始化
	model = tflearn.DNN(net, tensorboard_verbose=0, tensorboard_dir="./tflearn_data/tflearn_logs/")

	model.load("./tflearn_data/tflearn_modes/2019-07-03 17.26.25.047838/comment_mode.tflearn")

	return model


def model_predict(model):
	Xnew = pd.Series(["不错 老师讲的很好", "老师给分有点差", "很好", "慎重慎重，课程内容很实用，但课程很枯燥"])

	vect = CountVectorizer(ngram_range=(1, 1), token_pattern=r'\b\w{1,}\b')
	vect.fit(Xnew)
	vocab = vect.vocabulary_

	def convert_X_to_X_word_ids(X):
		return X.apply(lambda x: [vocab[w] for w in [w.lower().strip() for w in x.split()] if w in vocab])

	X_Xnew_word_ids = convert_X_to_X_word_ids(Xnew)

	# 序列扩充
	X_Xnew_padded_seqs = pad_sequences(X_Xnew_word_ids, maxlen=20, value=0)

	Y = model.predict(X_Xnew_padded_seqs)
	print(Y)

if __name__ == '__main__':
	comments_list = get_comment_from_database()

	start_time = datetime.now()
	tflearn_model = machine_learning(comments_list)
	model_predict(tflearn_model)
	end_time = datetime.now()
	print("total time: " + str(end_time - start_time))