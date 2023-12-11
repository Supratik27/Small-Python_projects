# Importing required libraries
from email.message import EmailMessage
from Password import Password
import ssl
import smtplib

email_sender = "Supratiksengupta27@gmail.com"
email_password = Password
email_receivers = ["Supratiksengupta16@gmail.com", "tilehod636@lanxi8.com"]
email_subject = "Merry Christmas Greetings!!"
body = """Eat. Drink. Be Merry. Have a wonderful Christmas! 2k23

Regards,
Supratik
"""

email = EmailMessage()
email["From"] = email_sender
email["To"] = email_receivers
email["Subject"] = email_subject
email.set_content(body)

Context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=Context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receivers, email.as_string())
