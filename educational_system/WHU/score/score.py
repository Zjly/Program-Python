from urllib import parse, request

from educational_system.WHU.login import get_login_opener


def get_score(opener):
	grade_page = "http://218.197.150.140/servlet/Svlt_QueryStuScore"

	post_data = parse.urlencode({
		'year': "0",
		'term': "",
		'learnType': "",
		'scoreFlag': "0"
	})
	req = request.Request(grade_page, data=post_data.encode("gbk"))
	resp = opener.open(req)
	with open('score.html', "w", encoding="gbk") as fp:
		fp.write(resp.read().decode("gbk"))

def main():
	opener = get_login_opener("2017302580196", "zl19990105")
	get_score(opener)

if __name__ == '__main__':
	main()