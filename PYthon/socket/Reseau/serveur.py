
"""
    pour créer un serveur il faut nécéssairement passer par 4 étapes
    1: Créer le socket
    2: Donner les options au socket
    3: Lier à un port
    4: Ecouter après des connexions
"""
import socket,sys
# Les variables
host=""
"""
    host = socket.gethostbyname(socket.gethostname())
    Selection de l'interface réseau publique
"""
port=1234

#Création de socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Donner les options au socket
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# Lier à un port
s.bind((host,port))

# Ecouter après des connexions
s.listen(5)