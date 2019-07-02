from urllib import request
import requests
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

# ——————————————————————————————————————————

# url = "http://www.baidu.com"
#
# response = request.urlopen(url)
#
# html = response.read()
#
# # with open("./test1.txt", mode="wb") as fr:
# # 	fr.write(html)
#
# html = html.decode("utf-8")
# # print(html)
# # print(response.geturl())
#
# # head信息
# print(response.info())

# ——————————————————————————————————————————

# url = "http://www.baidu.com"
#
# r = requests.get(url)

# print(r.text)

# print(r.encoding)

# r.encoding = "utf-8"
# print(r.text)

# ——————————————————————————————————————————

# url = "http://ip.tool.chinaz.com/"
# r = requests.get(url)
#
# s = r.text
# print(r)
#
# pattern = "<dd class = \"fz24\">(.*?)</dd>"
# res = re.compile(pattern, re.S)
#
# print(res.findall(s))

# ——————————————————————————————————————————

# response = urlopen("http://www.weather.com.cn/weather/101200101.shtml")
#
# soup = BeautifulSoup(response, "html.parser")
#
# print(soup)

# ——————————————————————————————————————————
