* Etape 1
## Editer le fichier /etc/zabbix/zabbix_proxy.conf si utlisation du proxy  sinon /etc/zabbix/zabbix_server.conf
pour le cas du serveur  
```
SNMPTrapperFile=/tmp/zabbix_traps.tmp

#SNMPTrapperFile=/var/log/snmptrap/snmptrap.log

StartSNMPTrapper=1
```
enregistrer et quitter , puis:

```
(PROXY)
sudo systemctl restart zabbix-proxy 
ou 
(Server)
sudo systemctl restart zabbix-server
```

* Etape 2
```
sudo wget https://git.zabbix.com/projects/ZBX/repos/zabbix/raw/misc/snmptrap/zabbix_trap_receiver.pl -O /usr/bin/zabbix_trap_receiver.pl
```
* Etape 3

```
sudo chmod a+x /usr/bin/zabbix_trap_receiver.pl 
```
* Etape 4 Installation et configuration de snmptrapd

```
sudo apt install snmp, snmp-mibs-dowloader, snmptrapd
```
* Etape 5 Editer le fichier /etc/snmp/snmptrapd.conf et ajouter:
```
authCommunity execute afapark
perl do "/usr/bin/zabbix_trap_receiver.pl";
```
enregistrer et quitter , puis:
```

sudo systemctl restart snmptrapd

```
*****TEST*****
``` 
snmptrap -v2c -cafapark HOSTIP  ".1.3.6.1.6.3.1.1.5.3 .1.3.6.1.6.3.1.1.5.3 s "link down ewample v2c"

```

![image](https://user-images.githubusercontent.com/60136087/146380536-6333f1c1-a0ef-47a2-ae04-c26c5c5cfece.png)
