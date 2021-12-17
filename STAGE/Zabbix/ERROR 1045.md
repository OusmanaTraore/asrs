 # ERROR 1045 28000 Access denied for user 'root'@'localhost' using password NO  (Putty)
 * ETAPE 1
  ````
  mysqld_safe --skip-grant-tables
 
  service mysqld stop
  
  mysqld_safe --skip-grant-tables &
  
  ````
  
 * ETAPE 2 (ouvrir une autre session avec Putty)
 
  ````
  login :root
  password: <Enter>
  mysql -u root <Enter>
  
  ````
 * ETAPE 3
  
  ````
   mysql > use mysql;
   mysql > show tables ;
   mysql > desc user;
   mysql > Select User,Password,Host from user ;
   mysql > Update  mysql.user set Password=PASSWORD('root@123') where 'User=root' ;
   mysql > flush privileges;
   mysql > quit;
  
  ````
  * ETAPE 4 
   
  ````
    # service mysql start 
    # mysql -u root p 
     password: PASSWORD('root@123')
     
     mysql>
  ````
