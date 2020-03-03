import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Himanshu Gupta'
email['to'] = 'imhimansu28@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name':'TimTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp :
    smtp.ehlo()
    smtp.starttls( )
    smtp.login('webdevhimanshu@gmail.com', 'sxyklceinziaegys')
    smtp.send_message(email)
    print('all good boss! ')