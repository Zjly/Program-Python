import json
from urllib import parse
from urllib import request
from http.cookiejar import CookieJar

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

url = 'https://taoke.ziqiang.net.cn/api/course/public/elective/20182022196/'

# 创建一个cookieJar对象
cookieJar = CookieJar()

# 使用cookieJar创建一个HTTPCookieProcessor对象
handler = request.HTTPCookieProcessor(cookieJar)

# 使用上一步创建的handler创建一个opener
opener = request.build_opener(handler)

opener.open(request.Request(url))

post_data = parse.urlencode({
	'page': 1,
	'per_page': 20
})
req = request.Request(url, headers=headers)
resp = opener.open(req)

web_data = resp.read()
data = json.loads(web_data)
print(data)
# news = data['pagination']['public_elective']

# for n in news:
# 	title = n['title']
# 	img_url = n['image_url']
# 	url = n['media_url']
# 	print(url, title, img_url)
