#邮件的发送方（发送方地址、发送方客户端授权密码lqeeyexqynzqbged，SMTP服务器地址smtp.qq.com）
#装pip包 pip install pyemail 
#邮件内容
#邮件接收方腾讯QQ邮件设置
import smtplib #引入包
from email.mime.text import MIMEText #引入包
msg_from="chenshouquan@foxmail.com"#发送方
pwd="lqeeyexqynzqbged"#授权码
to="chenshouquan@foxmail.com"
subject="这是Python发送的邮件！"
content="这是一封测试邮件，你收到邮件了么！"

#构造邮件
msg=MIMEText(content)#msg邮件对象
msg["Subject"]=subject
msg["From"]=msg_from
msg["To"]=to

ss=smtplib.SMTP_SSL("smtp.qq.com",465)
ss.login(msg_from,pwd)
ss.sendmail(msg_from,to,msg.as_string())#发送
