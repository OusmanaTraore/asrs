import sqlite3

connexion = sqlite3.connect('album2.db')
curseur= connexion.cursor()

# curseur.execute('SELECT * FROM artiste')

# artistes= curseur.fetchall()
# print(artistes)


albums_cd= curseur.execute('SELECT titre FROM album a JOIN artiste ar ON a.artiste_id= ar.artiste_id AND ar.nom = "Celine Dion"').fetchall()

print(albums_cd)
connexion.close()