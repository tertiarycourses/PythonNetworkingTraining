from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
from base64 import decodestring
import urllib

# Server port
PORT = 8000

class ServerHandler(BaseHTTPRequestHandler):

        def _set_headers(self):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

        def do_HEAD(self):
                self._set_headers()
  
      
        def do_POST(self):
                self._set_headers()
                print("in post method")
                self.data_string = self.rfile.read(int(self.headers['Content-Length']))

                self.send_response(200)
                self.end_headers()
                print(self.data_string)

Handler = ServerHandler

# Initialize server object
httpd = HTTPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
