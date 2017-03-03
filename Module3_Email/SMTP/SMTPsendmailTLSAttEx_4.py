#!/usr/bin/env python3
import os
import getpass
import re
import sys
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
def send_email(sender, recipient):
    """ Sends email message """
    msg = MIMEMultipart()
    msg['To'] = recipient
    msg['From'] = sender
    subject = input('Enter your email subject: ')
    msg['Subject'] = subject
    message = input('Enter your email message. Press Enter when finished. ')
    part = MIMEText('text', "plain")
    part.set_payload(message)
    msg.attach(part)
    # attach an image in the current directory
    filename = input('Enter the file name of a GIF image: ')
    path = os.path.join(os.getcwd(), filename)
    if os.path.exists(path):
        img = MIMEImage(open(path, 'rb').read(), _subtype="gif")
        img.add_header('Content-Disposition', 'attachment',filename=filename)
        msg.attach(img)
    # create smtp session
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.login(sender,"12345678test")
    session.ehlo
    # send mail
    session.sendmail(sender, recipient, msg.as_string())
    print("You email is sent to {0}.".format(recipient))
    session.quit()
    
if __name__ == '__main__':
    sender = input("Enter sender email address: ")
    recipient = input("Enter recipeint email address: ")
    send_email(sender, recipient)
    
    
#-----------------------------------------------
#pdf attachments

## Import smtplib for the actual sending function
#import smtplib

## For guessing MIME type
#import mimetypes

## Import the email modules we'll need
#import email
#import email.mime.application

## Create a text/plain message
#msg = email.mime.Multipart.MIMEMultipart()
#msg['Subject'] = 'Greetings'
#msg['From'] = 'xyz@gmail.com'
#msg['To'] = 'abc@gmail.com'

## The main body is just another attachment
#body = email.mime.Text.MIMEText("""Hello, how are you? I am fine.
#This is a rather nice letter, don't you think?""")
#msg.attach(body)

## PDF attachment
#filename='simple-table.pdf'
#fp=open(filename,'rb')
#att = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
#fp.close()
#att.add_header('Content-Disposition','attachment',filename=filename)
#msg.attach(att)

## send via Gmail server
## NOTE: my ISP, Centurylink, seems to be automatically rewriting
## port 25 packets to be port 587 and it is trashing port 587 packets.
## So, I use the default port 25, but I authenticate. 
#s = smtplib.SMTP('smtp.gmail.com')
#s.starttls()
#s.login('xyz@gmail.com','xyzpassword')
#s.sendmail('xyz@gmail.com',['xyz@gmail.com'], msg.as_string())
#s.quit()