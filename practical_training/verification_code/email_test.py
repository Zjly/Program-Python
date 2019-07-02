import smtplib
from email.mime.text import MIMEText

# 接收邮件地址
to_email = '942471854@qq.com'

# 发送者信
# 这是真实可用的邮箱账号密码，为方便他人请勿修改谢谢
# 如果真的想要一个免费测试邮箱，发邮件到li@latelee.org谢谢
smtpserver = 'smtp.qq.com'
snd_email = '2335333894@qq.com'#'test@latelee.org'
username = snd_email
password = b'iniypwofdosdeadb'#b'1qaz@WSX'

subject = 'python email test'

def send_email(to_list, sub, content):
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = sub
    #msg['From'] = email.utils.formataddr(('py发送者', snd_email)) # 发件人：py发送者<xxx@163.com>
    msg['From'] = snd_email
    msg['To'] = to_list
    #msg['Date'] = formatdate(localtime=True)

    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        #smtp.login(username, bytes.decode(base64.b64decode(password)))
        smtp.login(username, bytes.decode(password))
        smtp.sendmail(snd_email, to_list, msg.as_string())
        smtp.quit()
        return 0
    except Exception as e:
        print(str(e))
        return -1

# main...
if __name__ == '__main__':  
    if send_email(to_email, "hello", "hello world, this is a python email test") == 0:  
        print("send %s ok" % to_email)
    else:  
        print("send failed")