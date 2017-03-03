from smb.SMBConnection import SMBConnection
 
user = 'NAME'
password = 'PASSWORD'
client_machine_name = 'AsusK501Lx'
 
server_name = 'AsusK501Lx'
server_ip = '0.0.0.0'
 
domain_name = 'domainname'
 
conn = SMBConnection(user, password, client_machine_name, server_name)
conn.connect(server_name)


 
shares = conn.listShares()
 
for share in shares:
    if not share.isSpecial and share.name not in ['NETLOGON', 'SYSVOL']:
        sharedfiles = conn.listPath(share.name, '/')
        for sharedfile in sharedfiles:
            print(sharedfile.filename)
 
conn.close()
 
# with open('pysmb.py', 'rb') as file:
#     conn.storeFile('remotefolder', 'pysmb.py', file)