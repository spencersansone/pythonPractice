import smtplib
from email.mime.text import MIMEText

def sendGmail(info):
    msg = MIMEText(info['b'])
    msg['Subject'] = info['s']
    msg['From'] = info['g_sender']
    msg['To'] = info['r_email']
    try:
        print("Attempting to send, please wait...")
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(info['g_sender'], info['g_pass'])
        server.sendmail(info['g_sender'], info['r_email'], msg.as_string())
        server.close()
        print('Email sent!')
    except:
        print('Something went wrong...')

gmail_sender = input("Please enter your gmail address: ")
gmail_pass = input("Please enter your gmail password: ")
recipient_email = input("Please enter the recipient's email address: ")
subject = input("Please enter the subject: ")
body = input("Please enter the message: ")

info = {}
info['g_sender'] = gmail_sender
info['g_pass'] = gmail_pass
info['r_email'] = recipient_email
info['s'] = subject
info['b'] = body

sendGmail(info)

