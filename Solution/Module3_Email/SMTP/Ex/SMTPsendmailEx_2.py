#!/usr/bin/env python3
# Listing 1 – First email client
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465 
def send_email(sender, recipient):
    """ Send email message """
    msg = MIMEMultipart()
    msg['To'] = recipient
    msg['From'] = sender
    subject = input('Enter your email subject: ')
    msg['Subject'] = subject
    message = input('Enter your email message. Press Enter when finished. ')
    #part = MIMEText('text', "plain")
    #part.set_payload(message)
    part = MIMEText(message, "plain")
    msg.attach(part)
    # create smtp session
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.login(sender,"12345678test")
    session.set_debuglevel(1)
    # send mail
    session.sendmail(sender, recipient, msg.as_string())
    print("You email is sent to {0}.".format(recipient))
    session.quit()
if __name__ == '__main__':
    sender = input("Enter sender email address: ")
    recipient = input("Enter recipient email address: ")
    send_email(sender, recipient)    
