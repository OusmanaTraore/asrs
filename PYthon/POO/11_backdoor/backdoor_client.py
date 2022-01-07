# socket
#bind (ip,port) 127.0.0.1 -> localhost
# listen
#
#accept -> socket / (ip,port)
# close

import socket 
import time 

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
    reponse = commande
    s.sendall(reponse.encode())

s.close()

