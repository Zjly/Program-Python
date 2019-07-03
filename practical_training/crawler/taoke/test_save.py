import csv
import pandas as pd

test1 = ["a", "b", "c"]
test2 = ["d", "e", "f"]
test = [test1, test2]

with open("test.csv", "w", encoding="utf-8") as fp:
	for i in test:
		for j in range(len(i)):
			fp.write(i[j])
			if j != len(i) - 1:
				fp.write("|")
		fp.write("\n")

file = pd.read_csv("test.csv", sep="|", header=None)
print(file)
file = file
print(file[2][1])
print(len(file))
# for i in range(len(file)):
# 	for j in range(3):
# 		print(file[0][j])