import pandas as pd
import smtplib
from email.mime.text import MIMEText
import credentials

'''my_mail = 'your email'

my_pass = 'your password'

my_smtp = 'mail.gmx.net'

my_port = your email port

my_name = 'your name'

your_mail = 'the receivers email'
subject = 'subject'

if subject:
    Anrede = 'Herr/Frau'
    Name = 'nachname receiver '
    Art = 'Hiwi/Werkstudent/Praktikant'

message = f\'\'\'Sehr geehrter {Anrede} {Name},\n\nhiermit möchte ich mich für die {Art} Stelle bewerben. Sie finden die relevante Unterlagen im Anhang beigefügt. Vielen Dank im Voraus\n\nMit freundlichen Grüßen\nAC Mostafa  \'\'\' '''

#! ONLY WORKS IF YOU HAVE NO TWO FACTOR AUTHENTICATION!!!

try:
    message = credentials.message
    msg = MIMEText(message)
    msg['Subject'] = credentials.subject
    msg['From'] = credentials.my_mail
    msg['To'] = credentials.your_mail

    print('Starting Process')
    smtpObj = smtplib.SMTP(credentials.my_smtp, credentials.my_port)
    print('SMTP Object Made')
    smtpObj.ehlo()
    smtpObj.starttls()
    print('Logging in...')
    smtpObj.login(credentials.my_mail, credentials.my_pass)
    print('Logged in!')
    print('Sending Email...')
    smtpObj.sendmail(credentials.my_mail, credentials.your_mail, msg.as_string())
    print('Email Sent!')
    smtpObj.quit()
except smtplib.SMTPDataError as de:
    print(de)