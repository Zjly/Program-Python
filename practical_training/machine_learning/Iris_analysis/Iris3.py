import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.model_selection import train_test_split

iris = np.array(pd.read_csv('iris.csv'))
x_train, x_test, y_train, y_test = train_test_split(iris.data,
													iris.target,
													test_size=0.2,
													random_state=0)
