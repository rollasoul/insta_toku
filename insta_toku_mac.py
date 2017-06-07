import socket
import os
import subprocess
from subprocess import Popen, PIPE, STDOUT
import time

# timer triggers webcam to take image

s = socket.socket()
host = "147.75.73.29"
port = 12345
s.connect((host, port))

print "waiting for image"
os.chdir('/Users/rollasoul/')

while True:
        i=1
        f = open('haiku'+".png",'wb')
        i=i+1
        while (True):
        # receive and write file
                l = s.recv(1024)
                while (l):
                        f.write(l)
                        l = s.recv(1024)
                        print "file received"
                        s.send("file received")
                s.close()
                f.close()
                break
