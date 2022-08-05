from http.server import BaseHTTPRequestHandler, HTTPServer

class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)

        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("Hello, world!", "utf8"))
        return

port = 8080
server_address = ("0.0.0.0", port)
httpd = HTTPServer(server_address, HTTPServer_RequestHandler)

httpd.serve_forever()