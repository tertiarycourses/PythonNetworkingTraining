import getpass, imaplib
import email

M = imaplib.IMAP4_SSL('imap.gmail.com','993')
M.login("xxxxxxxx", "xxxxxxx")
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
        if part.get_content_type() == "text/plain": # ignore attachments/html
            body = part.get_payload(decode=True)
            save_string = str("Dumpgmailemail_" + str(num) + ".eml")
            # location on disk
            myfile = open(save_string, 'a')
            myfile.write(body.decode('utf-8'))
            # body is again a byte literal
            myfile.close()
        else:
            continue    
    
    

    #print('Message %s\n%s\n' % (num, data[0][1]))
    print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')

#typ, data1 = M.fetch(4, '(RFC822)')    
#raw_email = data1[0][1]
#print(raw_email)

#continue inside the same for loop as above
#raw_email_string = raw_email.decode('utf-8')
#print(raw_email_string)
## converts byte literal to string removing b''
#email_message = email.message_from_string(raw_email_string)
## this will loop through all the available multiparts in mail
#for part in email_message.walk():
    #if part.get_content_type() == "text/plain": # ignore attachments/html
        #body = part.get_payload(decode=True)
        #save_string = str("Dumpgmailemail_" + str(x) + ".eml")
        ## location on disk
        #myfile = open(save_string, 'a')
        #myfile.write(body.decode('utf-8'))
        ## body is again a byte literal
        #myfile.close()
    #else:
        #continue

    
M.close()
M.logout()