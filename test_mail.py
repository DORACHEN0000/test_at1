import smtplib, ssl 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender ="sterbule0607@gmail.com"
receiver = ['dora.chen@bluebirds.com.tw','a20022026@gmail.com']
passwd = "hzuz kcyu wuhu cwgz"
body = "This is send by python\nhow are you?"
for i in receiver:
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = i
    msg["subjest"] = Header("Test send email","utf-8").encode()


    msg_text=MIMEText(body)
    msg.attach(msg_text)
    c = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=c) as server:
        server.login(sender,passwd)
        server.sendmail(sender,i,msg.as_string())
print("success send mail")