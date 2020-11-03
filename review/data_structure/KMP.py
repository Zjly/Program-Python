def get_next(t):
	next = [-1]
	k = -1
	j = 0

	while j < len(t) - 1:
		if k == -1 or t[j] == t[k]:
			k += 1
			j += 1
			next.append(k)
		else:
			k = next[k]

	print(next)
	return next


def get_nextval(t):
	nextval = [-1]
	k = -1
	j = 0

	while j < len(t) - 1:
		if k == -1 or t[j] == t[k]:
			k += 1
			j += 1
			if t[j] != t[k]:
				nextval.append(k)
			else:
				nextval.append(nextval[k])

		else:
			k = nextval[k]

	print(nextval)
	return nextval


def KMP(s, t, next):
	i = 0
	j = 0

	while i < len(s) and j < len(t):
		if j == -1 or s[i] == t[j]:
			i += 1
			j += 1
		else:
			j = next[j]

	if j >= len(t):
		return i - len(t)
	else:
		return -1


if __name__ == '__main__':
	s = "aaabaaaab"
	t = "aaaab"
	next = get_next(t)
	next_val = get_nextval(t)
	result = KMP(s, t, next)
	print(result)
