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
    def __init__(self,nom):
        self.nom = nom
        print("Constructeur personne " + nom)
    def SePresenter(self):
        print("Bonjour je m'appelle " + self.nom )
    def Autrefonction(self):
        print(f"nom: {self.nom}")


#--- Utilisation
personne1 = Personne("Jean")  # je crée une personne
personne2 = Personne("titi")  # je crée une personne
personne1.SePresenter()
personne2.SePresenter()
