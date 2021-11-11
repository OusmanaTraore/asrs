def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom

def afficher_information_personne(nom,age):
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age + 1) + " ans")



def demander_age(nom_personne ):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " ,quel est votre age ? ")
        try: 
            age_int = int(age_str)
        except:
            print("Erreur: vous devez rentrer un nombre pour l'age")
    return age_int

# demander le nom 


nom1 = demander_nom()
nom2 = demander_nom()

age1 = demander_age(nom1)
age2 = demander_age(nom2)

afficher_information_personne(nom1,age1)
afficher_information_personne(nom2,age2)

