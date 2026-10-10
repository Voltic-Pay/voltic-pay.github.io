import http.server, socketserver, os

class H(http.server.SimpleHTTPRequestHandler):
    def send_error(self, code, message=None, explain=None):
        if code == 404 and os.path.exists("404.html"):
            body = open("404.html", "rb").read()
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)
        else:
            super().send_error(code, message, explain)

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", 8000), H) as s:
    s.serve_forever()
