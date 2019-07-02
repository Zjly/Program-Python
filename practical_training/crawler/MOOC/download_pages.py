import re
from urllib import request

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_driver = "C:\Program Files (x86)\Google\Chrome\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

def read_urls():
	"""
	得到储存在文件中的url列表
	:return:
	"""
	with open("./course_urls.csv", "r") as fp:
		urls = fp.readlines()

	for i in range(len(urls)):
		urls[i] = urls[i].replace("\n", "")

	# 去除重复地址
	urls = list(set(urls))
	return urls

def down_load_page(urls):
	for url in urls:
		req = request.Request(url=url, headers=headers)
		resp = request.urlopen(req)
		page_name = url.replace("http://www.icourse163.org/course/", "")

		with open(f"./course_data/{page_name}.html", "w", encoding="utf-8") as fp:
			fp.write(resp.read().decode('utf-8'))

if __name__ == '__main__':
	urls = read_urls()
	down_load_page(urls)
	driver.close()
