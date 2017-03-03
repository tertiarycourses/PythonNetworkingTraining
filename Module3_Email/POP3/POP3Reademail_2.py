#!/usr/bin/env python3
import getpass
import poplib
import email

GOOGLE_POP3_SERVER = 'pop.gmail.com'
POP3_SERVER_PORT = '995'
def fetch_email(username, password):
    mailbox = poplib.POP3_SSL(GOOGLE_POP3_SERVER,POP3_SERVER_PORT)
    mailbox.user(username)
    mailbox.pass_(password)
    num_messages = len(mailbox.list()[1])
    print("Total emails: {0}".format(num_messages))
    print("Getting last message")
    
    for i in range(1,num_messages+1):
        print("mail = ", i)
        for msg in mailbox.retr(i)[1]:
            raw_email=msg
            raw_email_string = raw_email.decode('utf-8')
            # converts byte literal to string removing b''
            email_message = email.message_from_string(raw_email_string) 
            #print(email_message)
    
            for part in email_message.walk():
                if part.get_content_type() == "text/plain": # ignore attachments/html
                    body = part.get_payload(decode=True)
                    print(body.decode('utf-8'))
                else:
                    continue 
            
    
    mailbox.quit()
    
    
    
if __name__ == '__main__':
    username = input("Enter your email user ID: ")
    password = getpass.getpass(prompt="Enter your email password:")
    username ="xxxxxxxx"
    password="xxxxxxxxx"    
    fetch_email(username, password)