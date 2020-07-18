import requests
import bs4

url = "http://ke.qq.com/course/list"

response = requests.get(url)
content_html = response.text
bs_content = bs4.BeautifulSoup(content_html, "html.parser")

# 获取最大页码
pages = bs_content.findAll(
	name="a",
	attrs={
		"class": "page-btn"
	}
)
page_num = pages[len(pages) - 1].text

data = []

def crawl_one_page(p):
	url = "http://ke.qq.com/course/list?page=" + str(p)
	response = requests.get(url)
	content_html = response.text
	bs_content = bs4.BeautifulSoup(content_html, "html.parser")

	list_course = bs_content.findAll(
		name="li",
		attrs={
			"class": "js-course-card-item"
		}
	)

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

for p in range(int(page_num)):
	crawl_one_page(p + 1)

print(data)