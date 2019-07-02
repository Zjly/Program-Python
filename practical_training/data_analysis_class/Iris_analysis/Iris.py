import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sb

# 读入数据
df = pd.read_csv('./iris.csv', header=None)

'''
数据时以逗号为分隔符的，
但是这个数据没有列的名字，
所以先给每个列取个名字，
直接使用数据说明中的描述
'''
df.columns = ['sepal_len', 'sepal_width', 'petal_len', 'petal_width', 'class']

# 查看前5条数据
# print(df.info())

'''
最后类别一列，感觉前面的'Iris-'有点多余
即把class这一列的数据按'-'进行切分
取切分后的第二个数据，为了好看一点点
'''
df['class'] = df['class'].apply(lambda x: x.split('-')[1])


# # 查看数据信息
# # print(df.describe())
#
# def scatter_plot_by_category(feat, x, y):
# 	# 透明度
# 	alpha = 0.5
# 	# 按照feat参数分组运算(class)
# 	gs = df.groupby(feat)
# 	cs = cm.rainbow(np.linspace(0, 1, len(gs)))
#
# 	for g, c in zip(gs, cs):
# 		plt.scatter(g[1][x], g[1][y], color=c, alpha=alpha)
#
#
# plt.figure()
# scatter_plot_by_category('class', 'sepal_len', 'petal_len')
# plt.xlabel('sepal_len')
# plt.ylabel('petal_len')
# plt.title('class')
#
# plt.figure()
# scatter_plot_by_category('class', 'sepal_width', 'petal_width')
# plt.xlabel('sepal_width')
# plt.ylabel('petal_width')
# plt.title('class')
#
# plt.figure()
# scatter_plot_by_category('class', 'sepal_len', 'petal_width')
# plt.xlabel('sepal_len')
# plt.ylabel('petal_width')
# plt.title('class')
#
# plt.figure()
# scatter_plot_by_category('class', 'petal_len', 'sepal_width')
# plt.xlabel('petal_len')
# plt.ylabel('sepal_width')
# plt.title('class')
#
# plt.show()


plt.figure(figsize=(20, 10))
for column_index, column in enumerate(df.columns):
	if column == 'class':
		continue
	plt.subplot(2, 2, column_index + 1)
	sb.violinplot(x='class', y=column, data=df)

plt.show()

# 首先对数据进行切分，即分出数据集和测试集
from sklearn.cross_validation import train_test_split

all_inputs = df[['sepal_len', 'sepal_width',
				 'petal_len', 'petal_width']].values
all_classes = df['class'].values

(X_train,
 X_test,
 X_train,
 Y_test) = train_test_split(all_inputs, all_classes, train_size=0.8, random_state=1)

# 使用决策树算法进行训练
from sklearn.tree import DecisionTreeClassifier

# 定义一个决策树对象
decision_tree_classifier = DecisionTreeClassifier()

# 训练模型
model = decision_tree_classifier.fit(training_inputs, training_classes)

# 所得模型的准确性
print(decision_tree_classifier.score(testing_inputs, testing_classes))

# 使用训练的模型进行预测，为了偷懒，
# 直接把测试集里面的数据拿出来了三条
print(X_test[0:3])
print(Y_test[0:3])
model.predict(X_test[0:3])