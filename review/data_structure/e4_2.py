s = "abcd"

length = 1
index = 0
max_length = 1
max_index = 0

for i in range(1, len(s)):
	if s[i] == s[i - 1]:
		length += 1
	else:
		if length > max_length:
			max_index = index
			max_length = length

		index = i
		length = 1

print(max_length, max_index)
