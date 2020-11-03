def hanoi1(n, x, y, z):
	if n == 1:
		print("将第", n, "个盘片从", x, "移到", z)
	else:
		hanoi1(n - 1, x, z, y)
		print("将第", n, "个盘片从", x, "移到", z)
		hanoi1(n - 1, y, x, z)


def hanoi2(n, x, y, z):
	stack = [[n, x, y, z]]
	while len(stack) != 0:
		task = stack.pop()
		if len(task) == 3:
			print("将第", task[0], "个盘片从", task[1], "移到", task[2])
		elif task[0] == 1:
			print("将第", task[0], "个盘片从", task[1], "移到", task[3])
		else:
			stack.append([task[0] - 1, task[2], task[1], task[3]])
			stack.append([task[0], task[1], task[3]])
			stack.append([task[0] - 1, task[1], task[3], task[2]])


if __name__ == '__main__':
	# hanoi1(3, "X", "Y", "Z")
	hanoi2(3, "X", "Y", "Z")
