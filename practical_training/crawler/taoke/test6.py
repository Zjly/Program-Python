import requests
import json

url = 'https://taoke.ziqiang.net.cn/api/course/public/elective/20182022196/'
web_data = requests.get(url).text
data = json.loads(web_data)

teacher = data["teacher"],
name = data["name"],
credit = data["credit"],
summary = data["summary"],
field = data["field"]
print(name, teacher, credit, field, summary)

	# news = data['data']['pc_feed_focus']
# for n in news:
# 	title = n['title']
# 	img_url = n['image_url']
# 	url = n['media_url']
# 	print(url, title, img_url)
