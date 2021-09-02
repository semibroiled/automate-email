#Import relevant libraries and packages
#Import Pandas to read and maneuver CSV files with data
import pandas as pd
#Use OS to automize getting filepath to avoid hardcodes
import os
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

#Get filepath for datasheet
cwd = os.getcwd()
files = []
for directory in os.listdir():
    if '.csv' in directory:
        files.append(cwd+'/'+directory)
for filename in files:
    if 'smtp' in filename:
        files.pop(files.index(filename))
#print(files) 

#Read CSV file
sheet_info = pd.read_csv(files[0]) #hardcoding filename for now out of test necessity. later add in user input to define filename

#Iterate through datarows
for i in range(len(sheet_info)):
    #Check if email to be sent
    if 'yes' in sheet_info.loc[i,'send'].strip().lower():
        #Making Message Body
        try:
            print('Making Message Body...')
            #Initialize Message Body
            if 'e' in str(sheet_info.loc[i,'anrede']):
                anrede = sheet_info.loc[i,'anrede']
            else:
                anrede = 'Damen und Herren'
            
            if str(sheet_info.loc[i,'nachname']) == 'nan':
                Nachname = None
            else:
                Nachname = str(sheet_info.loc[i,'nachname'])

            if 'dame' in anrede.lower():
                if Nachname:
                    opening = f'geehrte {anrede} {Nachname}'
                else:
                    opening = f'geehrte {anrede}'
            else:
                opening = f'geehrter {anrede} {Nachname}'
            
            Art = sheet_info.loc[i,'job']
            message = f'''Sehrs {opening},\n\nhiermit möchte ich mich für die {Art}stelle bewerben. Sie finden die relevante Unterlagen im Anhang beigefügt. Vielen Dank im Voraus\n\nMit freundlichen Grüßen\nAC Mostafa  '''
            print(message)   
            
            msg = MIMEText(message)
            msg['Subject'] = f"Bewerbung {Art}: {sheet_info.loc[i,'subject'].strip()}"
            msg['From'] = credentials.my_mail
            msg['To'] = sheet_info.loc[i,'email'].strip()
            
            #print(msg)
        except ValueError as ve:
            print(ve)
        
        #Adding Binary Attachments in the form of .pdf, .docx, and more

        #Connecting to Mail Server and sending Email
        try:
            #Connect to SMTP i.e. GMX Server
            print('Starting Process...')
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


#if __name__ == '__main__':
#    main()