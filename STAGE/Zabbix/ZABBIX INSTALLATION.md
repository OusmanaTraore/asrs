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
 
* ETAPE 2 (Zabbix front end) Dans la barre du navigateur executer http:<votre adresse IP>/zabbix
  Sur l'interface 
* f
* 

# Installation de l'agent zabbix
https://www.zabbix.com/download_agents?version=5.0+LTS&release=5.0.17&os=Linux&os_version=4.12&hardware=ppc64le&encryption=No+encryption&packaging=Archive&show_legacy=0

![image](https://user-images.githubusercontent.com/60136087/146176761-1654a251-0e92-430d-9335-2fa91d64957c.png)

![image](https://user-images.githubusercontent.com/60136087/146176857-cdf44185-c339-4db0-bbf8-252e0404efdb.png)

