#Requirements
https://www.zabbix.com/documentation/5.0/fr/manual/installation/requirements

![image](https://user-images.githubusercontent.com/60136087/146181058-cad902b2-d47c-44f7-9f06-6b03102d733b.png)

![image](https://user-images.githubusercontent.com/60136087/146181292-16a5498b-30b1-4616-8fa6-fe4f2f1cf341.png)

![image](https://user-images.githubusercontent.com/60136087/146181366-5d5b534f-8027-4977-80b4-949f93184f01.png)
![image](https://user-images.githubusercontent.com/60136087/146182979-ea1c4f04-49d2-44b2-9b23-d796546e833c.png)


Config personnnelle au niveau des VM
![image](https://user-images.githubusercontent.com/60136087/146181516-f928c649-5e36-4915-be7b-9b6415747209.png)
![image](https://user-images.githubusercontent.com/60136087/146181629-37788520-f485-49d8-b835-dee3fc97e78f.png)


# Lien officiel pour l'installation de Zabbix
https://www.zabbix.com/download?zabbix=5.0&os_distribution=ubuntu&os_version=20.04_focal&db=mysql&ws=apache

![image](https://user-images.githubusercontent.com/60136087/146175548-2b44da8f-e071-4851-9b26-32590b60dbe3.png)

![image](https://user-images.githubusercontent.com/60136087/146175630-016a91fb-f472-4b2f-bd87-c55e29d5e2c2.png)

![image](https://user-images.githubusercontent.com/60136087/146175697-21b20d7e-2c82-43d2-95bb-07feb54a7112.png)

![image](https://user-images.githubusercontent.com/60136087/146175778-8b0af32a-887f-42b6-b851-c949adead080.png)

* ETAPE 1 (se rendre dans la console et editer le fichier /etc/zabbix/zabbix_server.conf)
 ```
  sudo vim /etc/zabbix/zabbix_server.conf
 ```
 ajouter les lignes suivantes au fichier
 ```
 DBName=zabbix
 DBUser=zabbix
 DBPassword=<mot de passe de la base de donnée utilisé lors de la création avec mysql>
 ```
 enregister et quitter puis: 
 ```
 sudo systemctl restart zabbix-server.service
 ```
* ETAPE 2 (Zabbix Front end http://adresseIP/zabbix)

| Utilisateur | Admin  |
| ----------- | -----  |
|  Password   | zabbix | 

# Installation de zabbix-proxy sur le même serveur que zabbix (serveur de monitoring)
![image](https://user-images.githubusercontent.com/60136087/146201826-db1888aa-1f9a-444f-aaff-4b084a616b91.png)
 
 * ETAPE 1 Création d'une database propre à zabbix proxy
 ```
  mysql
  create database zabbix_proxy character set utf8 collate utf8_bin;
  grant all privileges on zabbix_proxy.* to zabbix@localhost;
  quit;
 ```
 
![image](https://user-images.githubusercontent.com/60136087/146204900-82d2c8f7-d1c3-4bff-852a-44b05e0da4ed.png)
  
 * ETAPE 2 Peuplement de la database
 ```
 cd /usr/share/doc/zabbix-proxy-mysql/
 zcat schema.sql.gz | mysql zabbix_proxy 
 ```
 * Etape 3 (configuration du fichier /etc/zabbix/zabbix_proxy
 ```
 DBName=zabbix_proxy
 DBUser=zabbix
 DBPassword=<mot de passe de la base de donnée utilisé lors de la création avec mysql>
 ListenPort=10055
 ```
 * Etape 4 (Démarrage de l'agent zabbix)
 ```
 sudo systemctl start zabbix-agent
 ```
# Installation de l'agent zabbix (machine à monitorée)
https://www.zabbix.com/download_agents?version=5.0+LTS&release=5.0.17&os=Linux&os_version=4.12&hardware=ppc64le&encryption=No+encryption&packaging=Archive&show_legacy=0

![image](https://user-images.githubusercontent.com/60136087/146176761-1654a251-0e92-430d-9335-2fa91d64957c.png)

![image](https://user-images.githubusercontent.com/60136087/146176857-cdf44185-c339-4db0-bbf8-252e0404efdb.png)

 * Etape 1 (après télechargement  du fichier tar.gz) décompresser le fichier
 ```
 wget https://cdn.zabbix.com/zabbix/binaries/stable/5.0/5.0.17/zabbix_agent-5.0.17-linux-4.12-ppc64le-static.tar.gz
 
 tar -xzvf ~/zabbix_agent-5.0.17-linux-4.12-ppc64le-static.tar.gz
 
 ```
  * Etape 2 (éditer le fichier /etc/zabbix/zabbix_agentd.conf
 ```
 Server=<adresse IP du serveur Zabbix>
 Hostname=<le nom de votre machine affiché via "hostname">
 ServerActive=<adresse IP du serveur Zabbix>
 
 ```
 enregistrer et quitter
 * Etape 3 (redémarrer l'agent )
  ```
  sudo systemctl restart zabbix-agent
  
  ou
  sudo systemctl restart zabbix-agent.service
 
 ```
 
