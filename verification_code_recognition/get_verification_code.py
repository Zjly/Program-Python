from http.cookiejar import CookieJar
from io import BytesIO
from urllib import request

import PIL.Image


def get_verification_code():
	"""
	从教务系统中获取图片并保存到本地
	:return:
	"""
	cookieJar = CookieJar()
	handler = request.HTTPCookieProcessor(cookieJar)
	opener = request.build_opener(handler)

	image_url = "http://218.197.150.140/servlet/GenImg"

	for i in range(100):
		res = opener.open(request.Request(image_url))
		temp_image = BytesIO(res.read())
		image = PIL.Image.open(temp_image)
		image.save(f"./images/未标注{i}.jpg")


if __name__ == '__main__':
	get_verification_code()
