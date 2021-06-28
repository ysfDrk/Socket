# Bismillahirrahmanirrahim
# Source : https://kerteriz.net/python-socket-programlama-nedir/
# Created by : Y.DORUK  
# Created Date : 26.06.2021  
#*******************************************************************
#**********************Server Socket Program ***********************

from os import pipe
import socket

host = "192.168.1.3"
port = 5555


    
# socket(family, type) : family parametresi AF_UNIX, AF_INET ve AF_INET6 değişkenlerini alabilir.
#AF_UNIX: UNIX domain protokolleri
#AF_INET: TCP ve UDP için IPv4 protokolleri
#AF_INET6: TCP ve UDP için IPv6 protokolleri

#type parametresi SOCK_STREAM, SOCK_DGRAM, SOCK_RAW, SOCK_RDM ve SOCK_SEQPACKET değişkenlerini alabilir.
#SOCK_STREAM: TCP bağlantı tipi
#SOCK_DGRAM: UDP bağlantı tipi
#SOCK_RAW: Henüz olgunlaşmamış soketler
#SOCK_RDM: Güvenilir datagramlar için
#SOCK_SEQPACKET: Bağlantı üzerinden kayıtlar için bir dizi transfer
try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print("Socket Created...") 
    s.bind((host,port))
    print("socket connected to number of {}...".format(port))

    s.listen(5) ## aynı anda en fazla 5 bağlantıya izin verdğimizi belirttik
    print("Listen to Socket")

except socket.error as msg:
    print("Hata:",msg)

while True:
    #Client ile bağlantı kurulursa
    c,addr=s.accept()
    print('Gelen bağlantı:', addr)

    #Bağlanan client tarafına hoşgeldin mesajı göndrelim
    message='Thank you for your connection'
    c.send(message.encode('utf-8'))

    c.close()


    
