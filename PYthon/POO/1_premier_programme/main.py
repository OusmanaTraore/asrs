def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom

def afficher_information_personne(nom,age ,taille =0):
    print()
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez %s ans "  % (age + 1))

    if age == 17:
        print("Vous êtes presque majeur ") 
    elif  age ==1 or age ==2:
        print("Vous êtes bébé ")
    elif 12 <= age < 18:
        print("Vous êtes adolescent ")
    elif age == 18:
        print("Tous juste majeur: Félicitations ")
    elif age > 60:
        print("Vous êtes sénior ")
    elif age < 10:
        print("Vous êtes enfant ")
    elif age >= 18:
        print("Vous êtes majeur ")
    else:
        print("Vous êtes mineur ")
    
    if not taille == 0:
        print("Votre taille : " + str(taille) + "m")




def demander_age(nom_personne ):
    age_int = 0
    while age_int == 0:
        age_str = input(f"{nom_personne} ,quel est votre age ? ")
        try: 
            age_int = int(age_str)
        except:
            print("Erreur: vous devez rentrer un nombre pour l'age")
    return age_int

# demander le nom 


# nom1 = demander_nom()
# nom2 = demander_nom()

nom1 = "personne1"
nom2 = "personne2"

age1 = demander_age(nom1)
age2 = demander_age(nom2)

afficher_information_personne(nom1,age1)
afficher_information_personne(nom2,age2)

NB_PERSONNNES = 3

for i in range (0, NB_PERSONNNES):
    nom = "personne" + str(i+1)
    age = demander_age(nom)
    afficher_information_personne(nom,age , 1.60)
