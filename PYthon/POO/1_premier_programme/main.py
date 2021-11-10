def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def demander_age():
    age_int = 0
    while age_int == 0:
        age_str = input("Quel est votre age ? ")
        try: 
            age_int = int(age_str)
        except:
            print("Erreur: vous devez rentrer un nombre pour l'age")
    return age_int

# demander le nom 


nom = demander_nom()
age = demander_age()

print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
print("L'an prochain vous aurez " + str(age + 1) + " ans")