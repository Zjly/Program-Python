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
	# 创建一个cookieJar对象
	cookieJar = CookieJar()

	# 使用cookieJar创建一个HTTPCookieProcessor对象
	handler = request.HTTPCookieProcessor(cookieJar)

	# 使用上一步创建的handler创建一个opener
	opener = request.build_opener(handler)

	return opener


def login(opener):
	"""
	发送账号密码验证码，登录教务系统
	:param opener:
	:return:
	"""
	# 登录地址
	login_url = 'http://218.197.150.140/servlet/Login'
	opener.open(request.Request(login_url))

	# 验证码地址
	imgurl = 'http://218.197.150.140//servlet/GenImg'
	userid = 2017302580196
	pwd = "75cac585284c550229df1a37a8b3bbb7"

	res = opener.open(request.Request(imgurl))
	tempIm = BytesIO(res.read())
	im = PIL.Image.open(tempIm)
	im.show()
	yzm = input("验证码：")

	post_data = parse.urlencode({
		'id': userid,
		'pwd': pwd,
		'xdvfb': yzm
	})

	req = request.Request(login_url, data=post_data.encode("gbk"), headers=headers)
	resp = opener.open(req)
	with open('login.html', "w", encoding="gbk") as fp:
		fp.write(resp.read().decode("gbk"))


def visit_home_page(opener):
	"""
	访问教务系统主页并下载源码
	:param opener:
	:return:
	"""
	homepage = "http://218.197.150.140/stu/stu_index.jsp"

	# 获取个人主页页面的时候，不要新建一个opener，而应该是用以前那个opener，因为之前的opener已经包含了登陆所需要的cookie信息
	req = request.Request(homepage, headers=headers)
	resp = opener.open(req)
	with open('home_page.html', "w", encoding="gbk") as fp:
		fp.write(resp.read().decode("gbk"))

def visit_grade_page(opener):
	"""
	访问教务系统成绩页面并下载源码
	:param opener:
	:return:
	"""
	grade_page = "http://218.197.150.140/servlet/Svlt_QueryStuScore"

	post_data = parse.urlencode({
		'year': "0",
		'term': "",
		'learnType': "",
		'scoreFlag': "0"
	})
	req = request.Request(grade_page, data=post_data.encode("gbk"), headers=headers)
	resp = opener.open(req)
	with open('grade_page.html', "w", encoding="gbk") as fp:
		fp.write(resp.read().decode("gbk"))

def visit_choose_page(opener):
	"""
	访问教务系统选课界面并下载源码
	:param opener:
	:return:
	"""
	choose_page = "http://218.197.150.140/stu/choose_PubLsn_list.jsp"

	file = []
	for i in range(1, 11):
		post_data = parse.urlencode({
			'XiaoQu': "0",
			'credit': "",
			'keyword': "",
			'pageNum': i
		})
		req = request.Request(choose_page, data=post_data.encode("gbk"), headers=headers)
		resp = opener.open(req)
		file.append(resp.read().decode("gbk"))

	with open('choose_page.html', "w", encoding="gbk") as fp:
		for f in file:
			fp.write(f)

if __name__ == '__main__':
	opener = get_opener()
	login(opener)
	visit_choose_page(opener)
