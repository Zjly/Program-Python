import json

import requests


def send1():
	headers = {
		"Cookie": "csrftoken=OtRSZCvfwh3iuH6WgzAVYjkYLAUIi4QG",
		"X-Csrftoken": "OtRSZCvfwh3iuH6WgzAVYjkYLAUIi4QG",
		"Referer": "https://taoke.ziqiang.net.cn/",
		"Content-Type": "application/json; charset=utf-8",
	}

	postdata = {
		"per_page": 20,
		"page": 3
	}

	posturl = 'https://taoke.ziqiang.net.cn/api/course/public/elective/'

	rep = requests.post(url=posturl, data=json.dumps(postdata), headers=headers)
	print(rep.text)


if __name__ == '__main__':
	send1()
