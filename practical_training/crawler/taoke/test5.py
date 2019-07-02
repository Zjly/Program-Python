import json
from urllib import request
from http.cookiejar import CookieJar

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

url = 'https://taoke.ziqiang.net.cn/api/course/public/elective/20182022196/'
cookieJar = CookieJar()
handler = request.HTTPCookieProcessor(cookieJar)
opener = request.build_opener(handler)
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
