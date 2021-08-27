import pandas as pd
import smtplib
import credentials

try:
    smtpObj = smtplib.SMTP(credentials.my_smtp, credentials.my_port)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(credentials.my_mail, credentials.my_pass)
    smtpObj.sendmail(credentials.my_mail, 'amitavmostafa137@gmail.com', f'''From: {credentials.my_name}<{credentials.my_mail}>
    To: Receiver<amitavmostafa137@gmail.com>
    Subject: Test 1 

    Dear me, wtf. Sincerely, You''')
    smtpObj.quit()
except smtplib.SMTPDataError as de:
    print(de)