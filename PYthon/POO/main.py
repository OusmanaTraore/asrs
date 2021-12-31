
#---- Definition----

class Personne:
    def __init__(self, nom: str="" , age: int=0 ):
        self.nom = nom   #
        self.age = age   # une variable d'instance : nom, age
        if nom =="":
            self.DemanderNom()
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        info_personne = "Bonjour je m'appelle " + self.nom 
        if self.age !=0:
            info_personne +=  ", j'ai " + str(self.age) + " ans"
        print (info_personne)

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
liste_personnes = [
    Personne("Jean", 30),
    Personne("Paul", 15),
    Personne("Zoe", 20)
]

for personne in liste_personnes:
    personne.SePresenter()
    print()

# personne1 = Personne("Jean",30 ,True)  # je crée une personne


# personne2 = Personne("titi",15)  # je crée une personne
# personne2.SePresenter()

# print('estMajeur1: ', personne1.EstMajeur())
# print("nom1: " + personne1.nom)