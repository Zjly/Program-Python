import requests
import bs4

data = []
url = "http://ke.qq.com/course/list"
res = requests.get(url)
content_html = res.text

# 构造bs的解析器
bs_content = bs4.BeautifulSoup(content_html, "html.parser")

list_course = bs_content.findAll(
	name="li",
	attrs={
		"class": "js-course-card-item"
	}
)

# 课程名 课程公司
for li in list_course:
	obj = {}
	course = li.find(
		name="a",
		attrs={
			"class": "item-tt-link"
		}
	)
	obj["course"] = course.text

	company = li.find(
		name="a",
		attrs={
			"class": "item-source-link"
		}
	)
	obj["company"] = company.text

	data.append(obj)

print(data)
