import random

yes = 0
sum = 0

for i in range(10000000):
	A_lackey = random.randint(1, 7)
	B_lackey = random.randint(1, 7)

	if A_lackey == 1 or B_lackey == 1:
		sum += 1
		if A_lackey == 1 and B_lackey == 1:
			yes += 1

print(yes / sum)