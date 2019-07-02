import json

from selenium import webdriver

url = "https://taoke.ziqiang.net.cn/#!/course/public/elective"

chrome_driver = "C:\Program Files (x86)\Google\Chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get(url)
a = driver.find_elements_by_class_name('td')
print(a)
driver.quit()
