import socket 
 
buf=1024 
adresse=('adresse_ip_serveur',20000) 
 
if __name__ == '__main__': 
    monSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    while True: 
        requete = raw_input('?: ').strip() 
        if requete=="": 
            break 
        monSocket.sendto("%s" % requete, adresse) 
        reponse, adr = monSocket.recvfrom(buf) 
        print ("=> %s" % reponse) 
    monSocket.close() 
    print ("fin du client UDP")
 