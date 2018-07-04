#required smtp library
import smtplib

def singleRecipientEmail(info):
    #formatted email message variable using sender email,
	#	recipient email, subject, and body
    email_text = """
    From: {}  
    To: {}  
    Subject: {}

    {}
    """.format(info[0], info[2], info[3], info[4])
    
    
    try:
		#smtp server info setup 
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		
		#test server contact
        server.ehlo()
		
		#attempt login
        server.login(info[0], info[1])
		
		#attempt to send message with sender email, recipient
		#email and formatted email message
        server.sendmail(info[0], info[2], email_text)
		
		#close connection
        server.close()

        print('Email sent!')
    except:
		#if server test, login attempt or send attempt fails...
		
        print('Something went wrong...')

#ask for needed information
gmail_email = input("Please enter your gmail address: ")
gmail_password = input("Please enter your gmail password: ")
recipient_email = input("Please enter the recipient's email address: ")
subject = input("Please enter the subject: ")
body = input("Please enter the message: ")

#email info array
#           0              1               2           3    4
info = [gmail_email,gmail_password,recipient_email,subject,body]

#utilize function
singleRecipientEmail(info)
