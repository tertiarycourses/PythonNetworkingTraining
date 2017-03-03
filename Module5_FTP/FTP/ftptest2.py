
import ftplib

filename = "download.txt"

ftp = ftplib.FTP("localhost")
ftp.login("Anonymous","")


#ftp.cwd('/pub/')

files = ftp.dir()
print(files)

#file = open('E:\_Training\Python_modules\FTP\mytest.txt','rb')                  # file to send
#ftp.storbinary('STOR mytest.txt', file)     # send the file

#download
file = open(filename ,'wb')
ftp.retrbinary("RETR " + filename ,file.write)


file.close()                                    # close file and FTP


ftp.quit()


# import ftplib
# session = ftplib.FTP('server.address.com','USERNAME','PASSWORD')
# file = open('kitten.jpg','rb')                  # file to send
# session.storbinary('STOR kitten.jpg', file)     # send the file
# file.close()                                    # close file and FTP
# session.quit()
