#!/usr/bin/python
import sys
import textwrap
import http.server
import socketserver

PORT = 8080


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(textwrap.dedent('''\
            <!doctype html>
            <html><head><title>It works V2</title></head>
            <body>
                <h1>XXXXXXXXXXX, I was on your disk and now I am in the cloud.</h1>
                <img src="https://i.gifer.com/3Bg5.gif" style="width: 500px;">
            </body>
            ''').encode('utf-8'))


def main():
    httpd = http.server.HTTPServer(("", PORT), Handler)
    print("serving at port", PORT)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
