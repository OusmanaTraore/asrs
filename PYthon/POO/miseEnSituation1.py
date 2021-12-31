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
    def __init__(self, nom: str  ,age: int, genre: bool):
        self.nom = nom   #
        self.age = age   # une variable d'instance : nom, age
        self.genre = genre
        if nom =="":
            self.DemanderNom()
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        print ("Bonjour je m'appelle " + self.nom + " j'ai " + str(self.age) + " ans")
        genre_str = "Masculin" if self.genre else "Feminin"
        print(f"Genre : {genre_str}")
        e_optionnel = "" if self.genre else "e"


        if self.EstMajeur():
            print("Je suis majeur"+ e_optionnel)
        else:
            print("Je suis mineur"+ e_optionnel)
        print()

    # est Majeur-> True/Fasle 
    def EstMajeur(self):
        return self.age >=18 
    
    def DemanderNom(self):
        self.nom = input("Nom de la personne nom: ")
#--- Utilisation
personne1 = Personne("Jean",30 ,True)  # je crée une personne
personne1.SePresenter()


# personne2 = Personne("titi",15)  # je crée une personne
# personne2.SePresenter()

# print('estMajeur1: ', personne1.EstMajeur())
# print("nom1: " + personne1.nom)