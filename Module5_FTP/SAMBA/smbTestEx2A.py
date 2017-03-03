from smb.SMBConnection import SMBConnection

user = 'NAME'
password = 'PASSWORD'
client_machine_name = 'AsusK501Lx'
server_name = 'AsusK501Lx'

smbcon = SMBConnection(user, password, client_machine_name, server_name)
smbcon.connect(server_name)

for share in smbcon.listShares():
    print(share.name)
    
smbcon.close()