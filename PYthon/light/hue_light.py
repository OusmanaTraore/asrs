from phue import Bridge
from ip_adress import bridge_ip_address

b = Bridge(bridge_ip_address)
b.connect()