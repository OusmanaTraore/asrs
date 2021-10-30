## Gestion des accents
# -*- coding: iso-8859-1 -*-

##importation de la bibliothèque socket
import socket 

##Création de l'objet socket en précisant IPv4(AF_INET) et le protocole TCP(SOCK_STREAM)  UDP:SOCK_DGRAM
print ('creation du socket ...' )
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
print ('socket fait') 

##Connexion à l'hôte distant
print ('connexion a l''hote distant'  )
s.connect(('www.eni.fr',80)) 
print ('connexion faite' )

##Echange de données
s.send('GET /index.html HTML/1.0\r\n\r\n')

# boucle permettant de récuperer la totalité des données
while 1:
    data=s.recv(128)
    print(data)
    if data=="":
        break
s.close()
