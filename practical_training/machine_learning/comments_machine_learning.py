import os
from datetime import datetime
import pandas as pd
import tflearn
from sklearn import preprocessing
import jieba
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from tflearn.data_utils import to_categorical, pad_sequences


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
	data["cut_comment"] = data.comment.apply(chinese_word_cut)

	# 确定评论部分(X)和标签部分(y)
	X = data["cut_comment"]
	y = data["evaluation"]

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
	vect.fit(X_train)

	# 设置dict，对每个出现的词语给予一个值
	vocab = vect.vocabulary_

	def convert_X_to_X_word_ids(X):
		"""
		将评论(文字部分)转化为id集(数值序列)
		:param X:评论集合
		:return:数值序列
		"""
		return X.apply(lambda x: [vocab[w] for w in [w.lower().strip() for w in x.split()] if w in vocab])

	# 转化评论到标签
	X_train_word_ids = convert_X_to_X_word_ids(X_train)
	X_test_word_ids = convert_X_to_X_word_ids(X_test)

	# 序列扩充，统一延长到长度为20的序列，使得评论序列格式相同，不足的用0代替
	X_test_padded_seqs = pad_sequences(X_test_word_ids, maxlen=20, value=0)
	X_train_padded_seqs = pad_sequences(X_train_word_ids, maxlen=20, value=0)

	# 标签集处理，将标签转化为类别向量
	unique_y_labels = list(y_train.value_counts().index)
	le = preprocessing.LabelEncoder()
	le.fit(unique_y_labels)

	# 将标签集类别向量转化为二进制矩阵[1, 0]和[0, 1]
	y_train = to_categorical(y_train.map(lambda x: le.transform([x])[0]), nb_classes=len(unique_y_labels))
	y_test = to_categorical(y_test.map(lambda x: le.transform([x])[0]), nb_classes=len(unique_y_labels))

	# 构造神经网络
	n_epoch = 100
	size_of_each_vector = X_train_padded_seqs.shape[1]
	vocab_size = len(vocab)
	no_of_unique_y_labels = len(unique_y_labels)

	net = tflearn.input_data([None, size_of_each_vector])
	net = tflearn.embedding(net, input_dim=vocab_size, output_dim=128)
	net = tflearn.lstm(net, 128, dropout=0.6)
	net = tflearn.fully_connected(net, no_of_unique_y_labels, activation='softmax')
	net = tflearn.regression(net, optimizer='adam', learning_rate=1e-4, loss='categorical_crossentropy')

	# 训练网络初始化
	model = tflearn.DNN(net, tensorboard_verbose=0, tensorboard_dir="./tflearn_data/tflearn_logs/")

	# 训练
	model.fit(X_train_padded_seqs, y_train, validation_set=(X_test_padded_seqs, y_test), n_epoch=n_epoch,
			  show_metric=True, batch_size=100)

	# 保存模型，按照时间戳、迭代次数和随机数种子建立并命名文件夹
	time = datetime.now()
	time_str = str(time).replace(":", ".")
	os.makedirs(f"./tflearn_data/tflearn_models/{time_str}({n_epoch}, {random_state})")
	model.save(f"./tflearn_data/tflearn_models/{time_str}({n_epoch}, {random_state})/model")


if __name__ == '__main__':
	comments_data = pd.read_csv("comments.csv")

	start_time = datetime.now()
	machine_learning(comments_data)
	end_time = datetime.now()
	print("total time: " + str(end_time - start_time))
