#usr/bin/env python3
import getpass
import imaplib
import pprint
import email

GOOGLE_IMAP_SERVER = 'imap.gmail.com'
IMAP_SERVER_PORT = '993'
def check_email(username, password):
    mailbox = imaplib.IMAP4_SSL(GOOGLE_IMAP_SERVER,IMAP_SERVER_PORT)
    #mailbox = imaplib.IMAP4(GOOGLE_IMAP_SERVER,IMAP_SERVER_PORT)
    mailbox.login(username, password)
    tmp1, data1 =mailbox.select('Inbox')
    num_msgs = int(data1[0])
    print('There are {} messages in INBOX'.format(num_msgs))    
    
    tmp, data = mailbox.search(None, 'ALL')
    print(">>",data)
    print(data[0].split())
    
    ##read the second email
    tmp, data = mailbox.fetch(b'1', '(RFC822)')
    print(data)
    print("-----------------------------")
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    pprint.pprint(raw_email_string)
 

    mailbox.close()
    mailbox.logout()

if __name__ == '__main__':
    username = input("Enter your email username: ")
    password = getpass.getpass(prompt="Enter you account password:")
    username="xxxxxxxx"
    password="xxxxxxx"
    check_email(username, password)    
