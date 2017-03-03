import poplib
from email import parser

pop_conn = poplib.POP3_SSL('pop.gmail.com','995')
pop_conn.user('xxxxxxx')
pop_conn.pass_('xxxxxxx')
#Get messages from server:
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
#print(messages)
#print(messages[0][1])
# Concat message pieces:
messages = ["\n".join(mssg[1]) for str(mssg) in messages]
#print(messages)
##Parse message intom an email object:
messages = [parser.Parser().parsestr(mssg) for mssg in messages]
print(messages)
for message in messages:
    print(">>>",message['subject'])
pop_conn.quit()