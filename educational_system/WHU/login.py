import hashlib
from io import BytesIO
from urllib import parse
from urllib import request
from http.cookiejar import CookieJar
import PIL.Image


headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

def get_opener():
	"""
	获取opener对象，存有cookies
	:return:
	"""
	cookieJar = CookieJar()
	handler = request.HTTPCookieProcessor(cookieJar)
	opener = request.build_opener(handler)

	return opener


def login(opener, id, password):
	"""
	发送账号密码验证码，登录教务系统
	:param opener:
	:return:
	"""
	login_url = 'http://218.197.150.140/servlet/Login'
	opener.open(request.Request(login_url))

	# 验证码
	img_url = 'http://218.197.150.140//servlet/GenImg'
	res = opener.open(request.Request(img_url))
	tempIm = BytesIO(res.read())
	im = PIL.Image.open(tempIm)
	im.show()
	yzm = input("验证码：")

	# post的参数
	post_data = parse.urlencode({
		'id': id,
		'pwd': hashlib.md5(password.encode()).hexdigest(),
		'xdvfb': yzm
	})

	req = request.Request(login_url, data=post_data.encode("gbk"), headers=headers)
	resp = opener.open(req)

def get_login_opener(id, password):
	opener = get_opener()
	login(opener, id, password)
	return opener