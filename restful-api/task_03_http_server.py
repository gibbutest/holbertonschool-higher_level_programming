from http.server import HTTPServer, BaseHTTPRequestHandler
import json

data = {"name": "John", "age": 30, "city": "New York"}

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()

            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()

            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            self.wfile.write(b"Page Not Found")



server = HTTPServer(('', 8000), MyServer)
print('Starting server...')

server.serve_forever()
server.server_close()

print('Stopping server...')