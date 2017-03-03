#usr/bin/env python3
import getpass
import imaplib
import pprint
import email

GOOGLE_IMAP_SERVER = 'imap.gmail.com'
IMAP_SERVER_PORT = '993'
def check_email(username, password):
    mailbox = imaplib.IMAP4_SSL(GOOGLE_IMAP_SERVER,IMAP_SERVER_PORT)
    mailbox.login(username, password)
    tmp1, data1 =mailbox.select('Inbox')
    num_msgs = int(data1[0])
    print('There are {} messages in INBOX'.format(num_msgs))    
    
    tmp, data = mailbox.search(None, 'ALL')
    print(">>",data)
    print(data[0].split())
    
    #read the first email
    tmp, data = mailbox.fetch(b'1', '(RFC822)')
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    #pprint.pprint(raw_email_string)
    # converts byte literal to string removing b''
    email_message = email.message_from_string(raw_email_string)
    
    for part in email_message.walk():
        print(part)
        if part.get_content_type() == "text/plain": # ignore attachments/html
            body = part.get_payload(decode=True)
            print(body.decode('utf-8'))
        else:
            continue       
    
    mailbox.close()
    mailbox.logout()

if __name__ == '__main__':
    username = input("Enter your email username: ")
    password = getpass.getpass(prompt="Enter you account password:")
    username="xxxxxxx"
    password="xxxxxx"
    check_email(username, password)    
