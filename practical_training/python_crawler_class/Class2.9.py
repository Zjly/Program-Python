from urllib import request

dapeng_url = "https://taoke.ziqiang.net.cn/api/course/public/elective/20182022196/"
headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

req = request.Request(url=dapeng_url, headers=headers)
resp = request.urlopen(req)
with open('renren.html', 'w', encoding='utf-8') as fp:
	fp.write(resp.read().decode('utf-8'))
