from http.server import HTTPServer, BaseHTTPRequestHandler
import time
import cgi
import flask

hostname = "localhost"
serverPort = 8080


class HomeServer01(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == '/':
            self.path = '/Index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File Not Found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

    def do_POST(self):
        if self.path.endswith('/new'):
            file_to_open = self.content
            self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


httpd = HTTPServer(('localhost', 8080), HomeServer01)
print('Server running on port %s' % serverPort)
httpd.serve_forever()


