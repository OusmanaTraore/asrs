"""def afficher_information_personne(nom, age):
    print(f"la personne s'appelle {nom}, son age est {age} ans")


def demander_nom_personne():
    nom = input('quel est votre nom?')
    return nom

nom1 = "jean"
age1 = 30


afficher_information_personne("ousmana", 37)

demander_nom_personne()"""
#---- Definition----

class Personne:
    def __init__(self, nom: str ):
        self.nom = nom   #
        

    def SePresenter(self):
        print ("Bonjour je m'appelle " + self.nom )
        
#--- Utilisation

nombre_de_personnes = 3

liste_personnes = []

for i in range(nombre_de_personnes):
    nom = input("nom de la personne " + str(i+1) + " : ")
    liste_personnes.append(Personne(nom))

for personne in liste_personnes:
    personne.SePresenter()


# personne2 = Personne("titi",15)  # je crée une personne
# personne2.SePresenter()

# print('estMajeur1: ', personne1.EstMajeur())
# print("nom1: " + personne1.nom)