# Bismillahirrahmanirrahim
# Source : https://kerteriz.net/python-socket-programlama-nedir/
# Created by : Y.DORUK  
# Created Date : 26.06.2021  
#*******************************************************************
#**********************Client Socket Program ***********************

import socket

s=socket.socket()

host="localhost"
port=5555

try:
    s.connect((host,port))

    yanit=s.recv(1024)
    print(yanit.decode("utf-8"))

    s.close()

except socket.error as msg:
    print("[Server deactive.] Message: ",msg)
    

