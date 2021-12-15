# POUR L'INSTALLATION DE ZABBIX SERVER VERSION 5.0
## DISTRIBUTION UBUNTU 20.04 (FOCAL)
  * ETAPE 1 (Obtention des Packages et Installation)
   ```
  wget https://repo.zabbix.com/zabbix/5.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_5.0-1+$(lsb_release -sc)_all.deb

  sudo dpkg -i zabbix-release_5.0-1+$(lsb_release -sc)_all.deb
  
  sudo apt update
  
  sudo apt -y install zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-agent
   ```
  * ETAPE 2 (Configuration de la DataBase)
       a. Installation de MariaDB
       ```
       sudo apt -y install mariadb-common mariadb-server-10.3 mariadb-client-10.3
       
       sudo systemctl start mariadb
       
       sudo systemctl enable mariadb
       
       ```
       b. Reset du mot de passe de la Database
       ```
       sudo mysql_secure_installation
       
       
       ```
       c.


  * ETAPE 2 (Configuration de la DataBase)
  * ETAPE 2 (Configuration de la DataBase)
  * ETAPE 2 (Configuration de la DataBase)






# POUR L'INSTALLATION DE ZABBIX AGENT
# POUR L'INSTALLATION DE ZABBIX PROXY
