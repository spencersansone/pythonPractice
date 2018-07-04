import smtplib

def singleRecipientEmail(info):
    email_text = """
    From: {}  
    To: {}  
    Subject: {}

    {}
    """.format(info[0], info[2], info[3], info[4])
    
    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(info[0], info[1])
        server.sendmail(info[0], info[2], email_text)
        server.close()
        print('Email sent!')
    except:  
        print('Something went wrong...')

gmail_email = input("Please enter your gmail address: ")
gmail_password = input("Please enter your gmail password: ")
recipient_email = input("Please enter the recipient's email address: ")
subject = input("Please enter the subject: ")
body = input("Please enter the message: ")

#           0              1               2           3    4
info = [gmail_email,gmail_password,recipient_email,subject,body]

singleRecipientEmail(info)
