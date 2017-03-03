import paramiko
 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
        ssh.connect('127.0.0.1', username='xxxxxx', password='xxxxxx')
except paramiko.SSHException:
        print("Connection Failed")
        quit()
 
#stdin,stdout,stderr = ssh.exec_command("ls -l")
stdin,stdout,stderr = ssh.exec_command("pwd")

 
for line in stdout.readlines():
        print(line.strip())
ssh.close()
