import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
from pyqrcode import QRCode
import png
import os


PORT = 8010

os.environ['USERPROFILE']
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive')
os.chdir(desktop)

Handler = http.server.SimpleHTTPRequestHandler

hostname = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" +str(PORT)
link = IP

url = pyqrcode.create(link)

url.svg("myqr.svg", scale=8)
webbrowser.open('myqr.svg')

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    print("Type this in your browser", IP)
    

