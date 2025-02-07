import smtplib
import ssl
import base64
from email.message import EmailMessage
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

email_sender = ''
#Use the following link to generate an app password
#https://myaccount.google.com/apppasswords
#something new here

app_password = ''
email_receiver = ''

subject = 'SMTP Test: Text message'
body = """  This is a test email implementing smtp protocol """

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
  smtp.login(email_sender, app_password)
  smtp.sendmail(email_sender, email_receiver, em.as_string())
  smtp.quit()

