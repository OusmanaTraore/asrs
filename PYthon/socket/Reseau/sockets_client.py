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
    data_recues = s.recv(MAX_DATA_SIZE)
    if not data_recues:
        break
    print("Message: ", data_recues.decode())
    texte_envoye = input("Vous: ")
    s.sendall(texte_envoye.encode())

s.close()

