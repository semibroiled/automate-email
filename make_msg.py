def make_msg(csvfile,i):
    '''Inputs are a read csvfile from pandas and the row iteration in script. Outputs message body'''

    try:
        #Initialize Message Body
        if csvfile.loc[i,'anrede']:
            anrede = csvfile.loc[i,'anrede']
        else:
            anrede = 'Damen und Herren'
        Nachname = csvfile.loc[i,'nachname']

        if 'dame' in anrede.lower():
            if Nachname:
                opening = f'geehrte {anrede} {Nachname}'
            else:
                opening = f'geehrte {anrede}'
        else:
            opening = f'geehrter {anrede} {Nachname}'
        Art = csvfile.loc[i,'job']
        message = f'''Sehr {opening},\n\nhiermit möchte ich mich für die {Art}stelle bewerben. Sie finden die relevante Unterlagen im Anhang beigefügt. Vielen Dank im Voraus\n\nMit freundlichen Grüßen\nAC Mostafa  '''
       
        msg = MIMEText(message)
        msg['Subject'] = csvfile.loc[i,'subject'].strip()
        msg['From'] = credentials.my_mail
        msg['To'] = csvfile.loc[i,'email'].strip()
        print(msg)
        return msg
    except:
        pass
        


def main(msg=''):
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