# Relever la liste des réseaux disponibles
Get-NetAdapter -Name *

#Supperession de la configuration IP de la carte de réseau
Remove-NetIPAddress -InterfaceIndex 22 -Confirm:$false

#Supperession de la configuration DNS de la carte de réseau
Remove-NetRoute -InterfaceIndex 22 -Confirm:$false

#Configuration d'une adresse IPV6 statique sur une interface
New-NetIPAddress -InterfaceIndex 22 -AddressFamily IPv6 -IPAddress aaaa::2 -PrefixLength 64 -DefaultGateway aaaa::1

#Configurer le serveur DNS d'un adaptateur réseau
Set-DnsClientServerAddress -InterfaceIndex 22 -ServerAddresses ("2001:4860:4860::8888","2001:4860:4860::8844")

#Vérification des adresse DNS configurée
Get-DnsClientServerAddress -InterfaceIndex 22

#Vérification des adresses  IP configurées
Get-NetIPConfiguration -InterfaceIndex 22 -Detailed

