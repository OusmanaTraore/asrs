""" Le protocole UDP (user Diaggram protocol) est un protocol qui se situe au même niveau que TCP
    Il est au dessus de la couche IP.
    Fournit un service en mode non-connecté aux applications.
    L'en-tête d'un diagramme UDP est composé de 4 champs
    1: port UDP-source
    2: port UDP-destination
    3: longueur du message UDP
    4: checksum (somme de contrôle)

    Le protocole est utilie et indispensable au bon fonctionnement d'internet
"""

## Gestion des accents
#--*--coding:UTF-8 --*--

# Création d'unb serveur synchrone (chaque requête doit attendre la fin du traitement de la requête précédente)
import socket,sys  
from math import *

buf =1024
adresse=('',2000)

socketserveur=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  

#utilisation de la méthode bind pour associer le port(2000) à l'adresse IP
socketserveur.bind(adresse)
print("serveur actif")

#boucle de service du serveur
while True:
    requete, adresseclient = socketserveur.recvfrom(buf)
    requete=requete.strip()
    try:
        reponse = "%s" %eval(requete)
    except:
        reponse = "%s" % sys.exc_info()[1]
    socketserveur.sendto("%s" % reponse,adresseclient)

# host=sys.argv[1]  
# textport=sys.argv[2]  
# try:  
#         port=int(textport)  
# except ValueError:  
#         port=socket.getservbyname(textport,'udp')  
# s.connect((host,port))  
# print("entrez les donnees a transmettre")  
# data=sys.stdin.readline().strip()  
# s.sendall(data)  
# print ("attente de reponse, Ctrl-C pour arreter")  
# while 1:  
#         buf=s.recv(2048)  
#         if not len(buf):  
#                 break  
#         print(buf)  