import smtplib
from email.mime.text import MIMEText

def send_alert(subject, body, to_email):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'you@example.com'
    msg['To'] = to_email

    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login('you@example.com', 'password')
    server.send_message(msg)
    server.quit()
