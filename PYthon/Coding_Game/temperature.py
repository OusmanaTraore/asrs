import random
from typing import Type
################################
# Variables
n = 50 
x=1
liste=[]
liste_postif=[]
liste_negatif=[]
liste_final=[]
####################################""
# Début du programme
while n > 0:
    e = random.randint(-273,5526)
    liste.append(e)
    n -=1
    x +=1
  
print(f"Liste de fin de boucle {x-1}:",liste)
for element in liste:
    if element > 0:
        liste_postif.append(element)
    elif element < 0 :
        liste_negatif.append(element)
    else:
        liste=[0]
print()
print(f"La liste_positif   : {liste_postif}")
print(f"Le min_positif   : {min(liste_postif)}")
print()
print(f"La liste_negatif   : {liste_negatif}")
print(f"Le max_negatif   : {max(liste_negatif)}")

max_negatif = max(liste_negatif)
min_positif = min(liste_postif)
valeur_absolue_max_negatif =  -max_negatif


print()
print(f"La valeur absolue du max_négatif   : {valeur_absolue_max_negatif}")
print()

print("====================")
print(f"min positif : {min_positif}")
print(f"max negatif : {valeur_absolue_max_negatif}")

print("====================")
liste_final.append(min_positif)
liste_final.append(valeur_absolue_max_negatif)
print(f"La liste finale : {liste_final}")
print("====================")
closest_temperature= min(liste_final)

print(f"La température la plus proche de zéro est  : {closest_temperature}")

