class Node:
	"""
	结点类
	"""

	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
		self.coding = ""


def calculate_frequency(string):
	"""
	计算字符串中各字符出现权值
	:param string: 字符串
	:return: 由[字符，出现权值]组成的键值对
	"""
	character_dict = dict()

	# 计算各字符出现次数
	for i in range(len(string)):
		current_character = string[i]

		if character_dict.__contains__(current_character):
			character_dict[current_character] += 1
		else:
			character_dict[current_character] = 1

	return character_dict


def create_tree(character_dict):
	"""
	创建哈夫曼树
	:param character_dict: 键值对
	:return: 哈夫曼树
	"""
	array = []
	for i in character_dict:
		array.append(Node([i, character_dict[i]]))

	# 只有一个字符
	if len(array) == 1:
		return array[0]

	# 创建哈夫曼树
	while len(array) != 1:
		least_node, less_node = find_min_node(array)
		father_node = Node(["", least_node.value[1] + less_node.value[1]], least_node, less_node)
		array.append(father_node)

	return array[0]


def find_min_node(array):
	"""
	找到数组中两个最小的结点
	:param array: Node数组
	:return: 最小节点, 次小节点
	"""
	# 寻找最小节点
	least = 0
	for i in range(len(array)):
		if array[i].value[1] < array[least].value[1]:
			least = i

	least = array[least]
	array.remove(least)

	# 寻找次小节点
	less = 0
	for i in range(len(array)):
		if array[i].value[1] < array[less].value[1]:
			less = i

	less = array[less]
	array.remove(less)

	return least, less


def get_huffman_dict(tree):
	"""
	得到字符对应的哈夫曼编码
	:param tree: 哈夫曼树
	:return: 由[字符，哈夫曼编码]组成的键值对
	"""
	huffman_dict = dict()
	traversing_grammar_tree(tree, huffman_dict)
	return huffman_dict


def traversing_grammar_tree(node, huffman_dict):
	"""
	先序遍历哈夫曼树并给予根节点哈夫曼编码
	:param node:
	:param huffman_dict:
	:return:
	"""
	# 遍历左子树
	if node.left is not None:
		node.left.coding += f"{node.coding}0"
		traversing_grammar_tree(node.left, huffman_dict)
	# 根节点设置哈夫曼编码
	else:
		huffman_dict[node.value[0]] = node.coding

	# 遍历右子树
	if node.right is not None:
		node.right.coding += f"{node.coding}1"
		traversing_grammar_tree(node.right, huffman_dict)
	# 根节点设置哈夫曼编码
	else:
		huffman_dict[node.value[0]] = node.coding


def huffman_coding(string, huffman_dict):
	"""
	生成哈夫曼编码
	:param string: 字符串
	:param huffman_dict: 哈夫曼dict
	:return: 哈夫曼编码
	"""
	result = ""
	for i in range(len(string)):
		character = string[i]
		coding = huffman_dict[character]
		result += coding
	return result


if __name__ == '__main__':
	c_string = "abbaabaaacc"
	c_dict = calculate_frequency(c_string)
	h_tree = create_tree(c_dict)
	h_dict = get_huffman_dict(h_tree)
	h_coding = huffman_coding(c_string, h_dict)
	print(f"字符串{c_string}的哈夫曼编码为{h_coding}")
