from io import BytesIO
from urllib import parse
from urllib import request
from http.cookiejar import CookieJar
import PIL.Image

headers = {
	"Accept": "application/json",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "zh-CN,zh;q=0.9",
	"Cache-Control": "no-cache",
	"Connection": "keep-alive",
	"Content-Length": "50",
	"Content-Type": "application/json",
	"Host": "taoke.ziqiang.net.cn",
	"Origin": "https://taoke.ziqiang.net.cn",
	"Pragma": "no-cache",
	"Referer": "http://taoke.ziqiang.net.cn/",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
	"X-CSRFToken": "Qr620ZTaeKJOnlbaiIvtx1WC62hzX3U7",
	"X-Requested-With": "XMLHttpRequest"
}


def get_opener():
	"""
	获取opener对象，存有cookies
	:return:
	"""
	# 创建一个cookieJar对象
	cookieJar = CookieJar()

	# 使用cookieJar创建一个HTTPCookieProcessor对象
	handler = request.HTTPCookieProcessor(cookieJar)

	# 使用上一步创建的handler创建一个opener
	opener = request.build_opener(handler)

	return opener


def login(opener):
	# 登录地址
	login_url = 'https://taoke.ziqiang.net.cn/#!/login'
	opener.open(request.Request(login_url))

	user_id = "2017302580196"
	pwd = "zl19990105"

	post_data = parse.urlencode({
		'number': user_id,
		'password': pwd
	})

	req = request.Request(login_url, data=post_data.encode("utf-8"), headers=headers)
	resp = opener.open(req)
	with open('login.html', "w", encoding="utf-8") as fp:
		fp.write(resp.read().decode("utf-8"))


if __name__ == '__main__':
	opener = get_opener()
	login(opener)
