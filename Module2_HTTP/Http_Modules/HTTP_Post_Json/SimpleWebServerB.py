#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import simplejson
import random
 
#Create custom HTTPRequestHandler class
class KodeFunHTTPRequestHandler(BaseHTTPRequestHandler):
  def _set_headers(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()

  def do_HEAD(self):
      self._set_headers()
  
  #handle GET command
  def do_GET(self):
    rootdir = 'e:/xampp/htdocs/' #file location
    try:
      if self.path.endswith('.html'):
        f = open(rootdir + self.path) #open requested file
        print("rootdir=",rootdir)
        print("Path=",self.path)
 
        #send code 200 response
        self.send_response(200)
 
        #send header first
        self.send_header('Content-type','text-html; charset=utf-8')
        self.end_headers()
 
        #send file content to client
        msg = f.read()
        self.wfile.write(msg.encode('utf-8'))
        f.close()
        return
      
    except IOError:
      self.send_error(404, 'file not found')

  def do_POST(self):
        self._set_headers()
        print("in post method")
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.end_headers()
        print(self.data_string)
        

        data = simplejson.loads(self.data_string)
        with open("test123456.json", "w") as outfile:
          simplejson.dump(data, outfile)
        print("{}".format(data))
        #f = open("for_presen.py")
        #self.wfile.write(f.read())
        return
  
def run():
  print('http server is starting...')
 
  #ip and port of servr
  #by default http server port is 80
  server_address = ('127.0.0.1', 80)
  httpd = HTTPServer(server_address, KodeFunHTTPRequestHandler)
  print('http server is running...')
  httpd.serve_forever()
  
if __name__ == '__main__':
  run()
