from urllib import request
from urllib import parse
from http.cookiejar import CookieJar

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}


def get_opener():
	# 创建一个cookieJar对象
	cookieJar = CookieJar()

	# 使用cookieJar创建一个HTTPCookieProcessor对象
	handler = request.HTTPCookieProcessor(cookieJar)

	# 使用上一步创建的handler创建一个opener
	opener = request.build_opener(handler)

	return opener


def login_renren(opener):
	# 使用opener发送登录请求
	data = {
		"email": "18268127804",
		"password": "zl526035"
	}

	login_url = "http://www.renren.com/PLogin.do"
	req = request.Request(login_url, data=parse.urlencode(data).encode("utf-8"), headers=headers)
	opener.open(req)


def visit_profile(opener):
	# 访问个人主页
	dapeng_url = "http://www.renren.com/880151247/profile"

	# 获取个人主页页面的时候，不要新建一个opener，而应该是用以前那个opener，因为之前的opener已经包含了登陆所需要的cookie信息
	req = request.Request(dapeng_url, headers=headers)
	resp = opener.open(req)
	with open('renren.html', "w", encoding="utf-8") as fp:
		fp.write(resp.read().decode("utf-8"))


if __name__ == '__main__':
	opener = get_opener()
	login_renren(opener)
	visit_profile(opener)
