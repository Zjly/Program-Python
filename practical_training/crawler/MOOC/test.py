import re

with open("./test.txt", "r", encoding="utf-8") as fp:
	course_data_html = fp.read()

pattern = "window.schoolDto = (.*?);"
p = re.compile(pattern, re.S)
course_school_range = p.findall(course_data_html)

pattern = "name\s*:\s*\"(.*?)\",\nbigLogo"
p = re.compile(pattern, re.S)
course_school = p.findall(course_school_range[0])
print(course_school)