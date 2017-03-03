import http.server
import socketserver
class myHandler(http.server.SimpleHTTPRequestHandler):
   def do_GET(self):
       print(self.path)
       self.send_response(301)
       new_path = '%s%s'%('http://pythoncodes.zohosites.com', self.path)
       self.send_header('Location', new_path)
       self.end_headers()

PORT = 8000
handler = socketserver.TCPServer(("127.0.0.1", PORT), myHandler)
print("serving at port 8000")
handler.serve_forever()
