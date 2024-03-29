import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost', 25)
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except smtplib.SMTPException:
   print("Error: unable to send email")