

#========================================================================

#run this on bash before starting for the fisrt time
#openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 365 -out server.crt

#========================================================================


import http.server
import ssl
import os

# Change directory to 'public' folder
os.chdir('public')

server_address = ('0.0.0.0', 4443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Use SSLContext instead of deprecated wrap_socket
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='../server.crt', keyfile='../server.key')
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"Serving on https://{server_address[0]}:{server_address[1]}")
httpd.serve_forever()
