import pandas as pd
import smtplib

smtpObj = smtplib.SMTP('mail.gmx.net', 587)

smtpObj.ehlo()

smtpObj.starttls()

smtpObj.login('yyy', 'xxx')
try:
    smtpObj.sendmail('xxx', 'xxx', '''From: Sender <xxx>
To: Receiver<xxx>
Subject: So long 

Dear me, wtf. Sincerely, You''')
except smtplib.SMTPDataError as de:
    print(de)
smtpObj.quit()