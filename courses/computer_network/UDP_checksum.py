def UDP_check():
	# 三个16比特的字
	num1 = 0b0110011001100000
	num2 = 0b0101010101010101
	num3 = 0b1000111100001100

	# 字之和
	check_sum = num1 + num2 + num3

	# 若有溢出进行回卷
	if check_sum > 0xffff:
		check_sum = ~check_sum

	# 检验四个数之和各位是否全为1
	if not ~(num1 + num2 + num3 + check_sum):
		print("校验通过")
	else:
		print("校验不通过")

def UDP_check8():
	# 三个8比特的字
	num1 = 0b01010011
	num2 = 0b01100110
	num3 = 0b01110100

	# 字之和
	check_sum = num1 + num2 + num3
	print(bin(check_sum))

	# 若有溢出进行回卷
	if check_sum > 0xff:
		check_sum = ~check_sum

	# 检验四个数之和各位是否全为1
	if not ~(num1 + num2 + num3 + check_sum):
		print("校验通过")
	else:
		print("校验不通过")

def test():
	num1 = 0b11011010
	num2 = 0b01100101
	sum = num1 + num2
	r_sum = ~sum
	print(bin(sum))
	print(bin(r_sum))

if __name__ == '__main__':
	UDP_check8()
