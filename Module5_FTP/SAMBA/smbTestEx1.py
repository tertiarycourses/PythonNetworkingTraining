
import  urllib.request 
from smb.SMBHandler import SMBHandler

director = urllib.request.build_opener(SMBHandler)
fh = director.open('smb://chee hong wee:sdu1620Xd@ASUSK501LX/testshare/file.txt')
print(fh.read())
fh.close()


