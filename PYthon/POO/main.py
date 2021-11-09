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
    def __init__(self,nom:str ,age: int):
        self.nom = nom   #
        self.age = age   # une variable d'instance : nom
        print("Constructeur personne " + nom)
    def SePresenter(self):
        print("Bonjour je m'appelle " + self.nom , "j'ai " + str(self.age) + " ans")


#--- Utilisation
personne1 = Personne("Jean",30)  # je crée une personne
personne2 = Personne("titi",25)  # je crée une personne
personne1.SePresenter()
personne2.SePresenter()

personne1.nom ="hgfg"
print("nom1: " + personne1.nom)