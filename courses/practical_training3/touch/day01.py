import torch
import matplotlib.pyplot as plt
import numpy

# 求导
# x = torch.tensor([5.0])
# x.requires_grad = True
# y = x ** 2
# y.backward()
# print(x.grad)
# --------------------------------------
# 求导
# x = 0
# grad_fn = lambda x: 2 * x - 2
# learning_rate = 0.01
# epoch = 500
# x_list = []
# for e in range(epoch):
# 	x_grad = grad_fn(x)
# 	x -= learning_rate * x_grad
# 	x_list.append(x)
# print(x)
# plt.plot(range(epoch), x_list)
# plt.show()
# --------------------------------------
# tensor

# x = torch.Tensor([0.0])
#
# learning_rate = 0.01
# epoch = 1000
# x_list = []
#
# for e in range(epoch):
# 	y = x ** 2 - 2 * x + 1
# 	y.backward(retain_graph=True)
# 	with torch.autograd.no_grad():
# 		x -= learning_rate * x.grad
# 		x_list.append(x.detach().clone().numpy())
# 		x.grad.zero_()

# --------------------------------------
import sklearn
import sklearn.datasets

data, target = sklearn.datasets.load_iris(return_X_y=True)
# print(data, target)
w = torch.randn(1, 4)
b = torch.randn(1)
y_ = torch.nn.functional.linear(input=x, weight=w, bias=b)
sy_ = torch.sigmoid(y_)
