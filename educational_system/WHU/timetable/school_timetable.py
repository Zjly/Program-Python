from urllib import request

from educational_system.WHU.login import get_login_opener


def get_timetable(opener):
	timetable_url = "http://218.197.150.140/servlet/Svlt_QueryStuLsn?csrftoken=a68bf89f-596c-38b0-b7c0-2503fb425b28&action=normalLsn&year=2018&term=2&state="
	res = opener.open(request.Request(timetable_url))
	with open('timetable.html', "w", encoding="gbk") as fp:
		fp.write(res.read().decode("gbk"))

if __name__ == '__main__':
	opener = get_login_opener("2017302580196", "zl19990105")
	get_timetable(opener)