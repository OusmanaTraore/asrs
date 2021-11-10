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
    def __init__(self,nom:str ="" ,age: int=0):
        self.nom = nom   #
        self.age = age   # une variable d'instance : nom
        self.genre = genre   # une variable d'instance : genre
        # if nom =="":
            # self.DemanderNom()
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        if self.genre:
            print("Bonjour, je m'appelle " + self.nom+ ",j'ai " + str(self.age) + "ans" )
            print("Genre : Masculin ")
        info_personne = "Bonjour je m'appelle " + self.nom 
        if self.age != 0:
            info_personne +=  "j'ai " + str(self.age) + " ans"
        print(info_personne)

        if self.age !=0:
            if self.EstMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")

    # est Majeur-> True/Fasle 
    def EstMajeur(self):
        return self.age >=18 
    
    def DemanderNom(self):
        self.nom = input("Nom de la personne nom: ")
#--- Utilisation
# personne1 = Personne("Jean",30)  # je crée une personne
# personne2 = Personne("titi",15)  # je crée une personne

personne3 = Personne()
personne4 = Personne()

personne1.SePresenter()
personne2.SePresenter()

# print('estMajeur1: ', personne1.EstMajeur())
# print("nom1: " + personne1.nom)