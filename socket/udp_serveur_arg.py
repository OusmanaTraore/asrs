#!/usr/bin/env python  
#--*-- coding:UTF-8 --*--  
import socket,sys  

# nom du hôte
host=sys.argv[1]

#numéro de port
textport=sys.argv[2] 

# nom du fichier qui se retouvera derrière le GET
fichier=sys.argv[3]  
try:  
    # connection via le protocole TCP
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  

        #vérification de la création du socket
except (socket.error,e):  
        print("erreur lors de la creation du socket : %s" %e)  
        sys.exit(1)  
try:  
        port=int(textport)  
        """ vérification du bon déroulement de port=int(textport),
            c'est à dire vérification de la transformation en nombre de la chaîne de caractères
        """
except ValueError:  
        try:  
                port=socket.getservbyname(host,'tcp')  
        except (socket.error,e):  
                print("ne trouve pas le port %s" %e)  
                sys.exit(1)  
try:  
        s.connect((host,port)) 
        """
            indication d'erreur d'adresse internet
        """
except (socket.gaierror, e):  
        print ("erreur d'adresse de connexion au serveur :%s" %e) 
        sys.exit(1)  

        """
        erreur de connexion ou d'envoi de donées
        """
except (socket.error, e):  
        print ("erreur de connexion: %s" %e)  
        sys.exit(1)  
try:  
        s.sendall("GET %s HTTP/1.0\r\n\r\n" % fichier)  
except (socket.error, e):  
        print ("erreur d'envoi des donnees : %s " %e)  
        sys.exit(1)  
while 1:  
        try:  
                buf=s.recv(2048)  
        except (socket.error, e):  
                print ("erreur de reception des donnees: %s" %e)  
                sys.exit(1)  
        if not len(buf):  
                break  
        print (buf) 