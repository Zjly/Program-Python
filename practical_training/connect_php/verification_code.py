# -*- coding:utf-8 -*-
import email
import random
import smtplib
from email.mime.text import MIMEText
import sys

# 发送邮件地址
smtp_server = 'smtp.qq.com'
snd_email = '2335333894@qq.com'
username = snd_email
password = b'iniypwofdosdeadb'


def send_email(to_list, sub, content):
	"""
	发送邮件
	:param to_list: 邮件地址
	:param sub: 邮件标题
	:param content: 邮件内容
	:return:
	"""
	msg = MIMEText(content, 'html', 'utf-8')
	msg['Subject'] = sub
	msg['From'] = email.utils.formataddr(('大学公共课程共享资源管理平台', snd_email))
	msg['To'] = to_list

	try:
		smtp = smtplib.SMTP_SSL()
		smtp.connect(smtp_server, 465)
		smtp.login(username, bytes.decode(password))
		smtp.sendmail(snd_email, to_list, msg.as_string())
		smtp.quit()
		return 0
	except Exception as e:
		print(str(e))
		return -1


def get_random_code(length):
	"""
	得到一个指定长度位数的验证码
	:param length: 指定长度
	:return: 得到的验证码
	"""
	code = ""
	for i in range(length):
		j = random.randint(0, 9)
		code = code + str(j)

	return code



if __name__ == '__main__':
	code = get_random_code(6)
	send_email(sys.argv[1], "大学公共课程共享资源管理平台——验证码", "<table class=\"responsive-table\" width=\"600\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" align=\"center\" valign=\"top\" bgcolor=\"#002650\" style=\"width: 600px; min-width: 600px; border-spacing: 0; border-collapse: collapse; margin: 0 auto; word-wrap: break-word; word-break: break-word; -ms-word-break: break-word; overflow-wrap: break-word; background-color: #002650;\"><tr><td class=\"body-text-section-padding-0px-15px-10px\" style=\"padding: 0;\" align=\"center\"><table class=\"responsive-table\" width=\"600\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\"><tr><td bgcolor=\"#002650\"><table width=\"100%\" cellspacing=\"0\" cellpadding=\"0\" border=\"0\" style=\"width: 100%; min-width: 100%; border-spacing: 0; border-collapse: collapse; word-wrap: break-word; word-break: break-word; -ms-word-break: break-word; overflow-wrap: break-word;\"><tr><td class=\"body-text-padding-0px-5p-30px-font-12px-left\" style=\"font-family: \'Open Sans\', Frutiger, \'Frutiger Linotype\', Univers, \'Helvetica Neue\', Helvetica, Arial, \'Gill Sans\', \'Gill Sans MT\', \'Myriad Pro\', Myriad, \'DejaVu Sans Condensed\', \'Liberation Sans\', \'Nimbus Sans L\', \'Malgun Gothic\', \'Microsoft YaHei\', AppleSDGothicNeo, AppleGothic, Dotum, \'Microsoft JhengHei\', \'Hiragino Kaku Gothic Pro\', \'Hiragino Kaku Gothic ProN W3\', Osaka, メイリオ, Meiryo, \'ＭＳ Ｐゴシック\', Calibri, Geneva, Display, Tahoma, Verdana, sans-serif; font-size: 14px; font-weight: 300; line-height: 24px; text-align: left; padding: 0 40px 40px; color: #bbbbbb;\"></br><table id=\"\" class=\"\" style=\"\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" height=\"\"><tr><td style=\"font-family: \'Open Sans\', Frutiger, \'Frutiger Linotype\', Univers, \'Helvetica Neue\', Helvetica, Arial, \'Gill Sans\', \'Gill Sans MT\', \'Myriad Pro\', Myriad, \'DejaVu Sans Condensed\', \'Liberation Sans\', \'Nimbus Sans L\', \'Malgun Gothic\', \'Microsoft YaHei\', AppleSDGothicNeo, AppleGothic, Dotum, \'Microsoft JhengHei\', \'Hiragino Kaku Gothic Pro\', \'Hiragino Kaku Gothic ProN W3\', Osaka, メイリオ, Meiryo, \'ＭＳ Ｐゴシック\', Calibri, Geneva, Display, Tahoma, Verdana, sans-serif;font-weight: 300; font-size: 24px; color: #FFFFFF; line-height: 32px;\">以下是您的验证码：</td></tr></table><p style=\"\"><em style=\"font-family: \'Open Sans\', Frutiger, \'Frutiger Linotype\', Univers, \'Helvetica Neue\', Helvetica, Arial, \'Gill Sans\', \'Gill Sans MT\', \'Myriad Pro\', Myriad, \'DejaVu Sans Condensed\', \'Liberation Sans\', \'Nimbus Sans L\', \'Malgun Gothic\', \'Microsoft YaHei\', AppleSDGothicNeo, AppleGothic, Dotum, \'Microsoft JhengHei\', \'Hiragino Kaku Gothic Pro\', \'Hiragino Kaku Gothic ProN W3\', Osaka, メイリオ, Meiryo, \'ＭＳ Ｐゴシック\', Calibri, Geneva, Display, Tahoma, Verdana, sans-serif;font-size: 28px; font-weight: 300; color: #3ed500; font-style: normal;\">" + str(code) + "</em></p><p style=\"\"> 您好！</p><p style=\"\"> 我们收到了来自您的安全请求，请使用上面的验证码验证您的账号归属。</p><p style=\"\"> <i><b>请注意：</b>不要将验证码告诉他人！</i></p><p style=\"\">代码全写队团队</p></td></tr></table></td></tr></table></td></tr></table>")
	print(code)