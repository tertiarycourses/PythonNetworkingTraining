import getpass, imaplib
import email

M = imaplib.IMAP4_SSL('imap.gmail.com','993')
M.login("xxxxx", "xxxxx")
M.select()
typ, data = M.search(None, 'ALL')
#print(data[0])

for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    # converts byte literal to string removing b''
    email_message = email.message_from_string(raw_email_string)
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            print(body.decode('utf-8'))
    print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')


M.close()
M.logout()
