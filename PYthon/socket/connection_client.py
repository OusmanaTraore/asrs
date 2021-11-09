#!/usr/bin/env python  
import socket,time  
  
host =socket.gethostbyname(socket.gethostname())  
print (host)  
port=1234  
 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  
s.bind((host,port))  
s.listen(1)  
 
client,adresse=s.accept()  
print (adresse) 
print ("une connexion s'est effectuee depuis ")  
print (client.getpeername())  
client.close()  
s.close()
 