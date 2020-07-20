import torchvision
import torch

from torchvision.datasets import MNIST
from torchvision.transforms import Compose, ToTensor

transform = Compose([ToTensor(), ])
train_mnist = MNIST(root="datasets", train=True, download=True, transform=transform)
print(len(train_mnist))
