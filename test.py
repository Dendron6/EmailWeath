import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
from paramWeather import *

def sendEmail():
    # section of retrieving pass and login
    file = pd.read_excel('notification.xlsx')
    email = file.username[0]
    password = file.password[0]

    # emailpart
    send_to_email = "deniskhomenko@yahoo.com"
    subject = "Weather update"
    message = condition()


    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = send_to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email,password)
    text = msg.as_string()
    server.sendmail(email,send_to_email,text)
    server.quit()

