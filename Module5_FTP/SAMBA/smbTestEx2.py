import  urllib.request 
from smb.SMBHandler import SMBHandler


file_fh = open('local_file.dat', 'rb')

director = urllib.request.build_opener(SMBHandler)
fh = director.open('smb://name:pwsd@ASUSK501LX/testshare/file1.txt', data = file_fh)

# Reading from fh will only return an empty string
fh.close()