import smtplib
import ssl
from email.message import EmailMessage
import os

# Configure sender email
email_sender = 'zjqrich@gmail.com'
# App password should be generated from Google Account settings
app_password = 'my_app_password_that_is_hidden'  # Remember to replace with your actual app password
# Multiple recipients
email_receivers = ['n01677466@humber.ca', 'zjqsmart@gmail.com']

# Email content
subject = 'Testing SMTP'
body = """
I am writing this email to test smtp, which is learned in class CPAN266 at Humber College.
"""

# Create the email message
em = EmailMessage()
em['From'] = email_sender
em['To'] = ', '.join(email_receivers)  # Join multiple recipients with commas
em['Subject'] = subject
em.set_content(body)

# Path to the text file you want to attach
file_path = 'attachment.txt'  # Replace with the actual path to your text file

# Read the file and add it as an attachment
with open(file_path, 'rb') as f:  # Note: 'rb' mode for binary reading
    file_data = f.read()
    file_name = os.path.basename(file_path)
    # This is the correct way to add an attachment in EmailMessage
    em.add_attachment(
        file_data,
        maintype='text',
        subtype='plain',
        filename=file_name
    )

# Create secure SSL context
context = ssl.create_default_context()

# Connect to Gmail's SMTP server and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    # Log in to the email account
    smtp.login(email_sender, app_password)
    # Send email to all recipients
    smtp.sendmail(email_sender, email_receivers, em.as_string())