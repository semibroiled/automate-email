#Import relevant libraries and packages
#Import Pandas to read and maneuver CSV files with data
import pandas as pd
#SMTP and email libraries will help connect to the Emails' Server and help build a modular email body
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#Credentials is a local Python file with...my credentials
import credentials

'''
credentials.py

my_mail = 'your email'

my_pass = input('Enter your password:\n') #Will ask for password after you import credentials

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

sheet_info = pd.read_csv()

#Initialize Message Body
message = credentials.message
msg = MIMEText(message)
msg['Subject'] = credentials.subject
msg['From'] = credentials.my_mail
msg['To'] = credentials.your_mail

def main():
    try:
        #Connect to SMTP i.e. GMX Server
        print('Starting Process')
        smtpObj = smtplib.SMTP(credentials.my_smtp, credentials.my_port)
        print('SMTP Object Made')
        smtpObj.ehlo()
        smtpObj.starttls()
        
        #Login
        print('Logging in...')
        smtpObj.login(credentials.my_mail, credentials.my_pass)
        print('Logged in!')
        
        #Send email
        print('Sending Email...')
        smtpObj.sendmail(credentials.my_mail, credentials.your_mail, msg.as_string())
        print('Email Sent!')
        smtpObj.quit()
    except smtplib.SMTPDataError as de:
        print(de)

if __name__ == '__main__':
    main()