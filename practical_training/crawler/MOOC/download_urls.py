import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_driver = "C:\Program Files (x86)\Google\Chrome\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)


def download_course_urls():
	"""
	下载课程的链接地址并保存到文件中
	:return:
	"""
	url = "http://www.icourse163.org/category/all"
	driver.get(url)

	course_url_list = []
	for i in range(5):
		page_html = driver.page_source
		course_url_list = course_url_list + get_course_url_from_page(page_html)

		next_button = driver.find_element_by_link_text("下一页")
		driver.execute_script("arguments[0].click();", next_button)

	with open("./course_urls.csv", "w") as fp:
		for url in course_url_list:
			fp.write("http://" + url + "\n")


def get_course_url_from_page(page_html):
	"""
	得到该页面中所有课程信息
	:param page_html: 页面html的源代码
	:return: 该页面中所有课程的链接list
	"""
	# 找到包含有课程链接的区域
	pattern = "<!--Regular if35-->(.*?)<!--Regular if43-->"
	p = re.compile(pattern, re.S)
	url_range = p.findall(page_html)

	# 对该区域内内容进行课程链接的匹配
	pattern = "<a href=\"//(.*?)\" target=\"_blank\">"
	p = re.compile(pattern, re.S)
	urls = p.findall(url_range[0])
	final_data = list(set(urls))
	return final_data


if __name__ == '__main__':
	download_course_urls()
	driver.close()
