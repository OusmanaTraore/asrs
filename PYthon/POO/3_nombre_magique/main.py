import random

def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int ==0 :
        nombre_str=input(f"Quel est le nombre magique (entre {nb_min} et {nb_max}) ? ")
        try:
            nombre_int = int(nombre_str)    
        except ValueError:
            print("ERREUR: Vous devez entrer un nombre entier! Reessayer !")
        else:
            if nombre_int < nb_min or  nombre_int> nb_max :
                print(f"ERREUR :  Le nombre doit être entre {nb_min} et {nb_max} . Reesayer !")
                nombre_int = 0

    return nombre_int



NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIC = random.randint(NOMBRE_MIN,NOMBRE_MAX)
NB_VIES = 4 

nombre=0
vies = NB_VIES  

# le nombre magic est plus petit
while not nombre == NOMBRE_MAGIC and vies >0 :
    print (f" Vous avez { vies } vies !")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)

    if nombre == NOMBRE_MAGIC:
        print("Bravo , vous avez trouvé le nombre magic !!!!")
        print(f"Le nombre magique etait: {NOMBRE_MAGIC}")
    elif nombre < NOMBRE_MAGIC:
        print("le nombre magic est plus grand")
        vies -= 1
    else:
        print("le nombre magic est plus petit")
        vies -= 1

if vies == 0:
    print("Vous avez perdu !")
    print(f"Le nombre magique etait: {NOMBRE_MAGIC}")