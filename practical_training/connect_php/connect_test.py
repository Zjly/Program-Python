import sys


def test(a, b):
	return int(a) + int(b)


if __name__ == "__main__":
	res = test(a=sys.argv[1], b=sys.argv[2])
	print(res)
