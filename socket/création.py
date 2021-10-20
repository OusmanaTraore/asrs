
import socket 
print ('creation du socket ...' )
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
print ('socket fait') 
print ('connexion a l''hote distant'  )
s.connect(('www.eni.fr',80)) 
print ('connexion faite' )