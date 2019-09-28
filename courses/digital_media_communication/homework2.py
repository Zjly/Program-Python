def run_length_encoding(strings):
	"""
	行程编码 RLE
	采用*+该字符重复个数+该字符来表示，不足4个字符表示为原字符
	例如aaaa表示为*4a，aabbbb表示为aa*4b
	:param strings: 原字符串
	:return: 压缩后的字符串
	"""
	# 当前字符重复个数
	length = 1

	# 结果串
	result = ""

	# 遍历字符串中的每一个字符进行编码
	for i in range(len(strings) - 1):
		# 重复字符
		if strings[i] == strings[i + 1]:
			length += 1
		# 非重复字符
		else:
			# 字符重复次数是否大于四进行不同的编码
			if length >= 4:
				result += f"*{length}{strings[i]}"
			else:
				for j in range(length):
					result += strings[i]

			# 重置字符串长度
			length = 1

	# 末尾字符处理
	if length != 1:
		result += f"*{length}{strings[len(strings) - 1]}"
	else:
		result += strings[len(strings) - 1]

	return result


if __name__ == '__main__':
	strings = input("输入待压缩的字符串: ")
	print("压缩后的字符串为: " + run_length_encoding(strings))
