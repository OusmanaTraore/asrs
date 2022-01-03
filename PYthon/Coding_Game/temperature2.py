import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
liste=[]
liste_postif=[]
liste_negatif=[]
liste_final=[]


n = int(input())  # the number of temperatures to analyse
if n==0:
    liste= 0
    print(liste)

for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    liste.append(t)

for element in liste:
    element = int(element)
    if element > 0:
        liste_postif.append(element)

    elif element < 0 :
        liste_negatif.append(element)
    else:
        liste=[]

if liste_negatif and liste_postif==[]:
    max_negatif = max(liste_negatif)
    print(max_negatif)
elif liste_postif and liste_negatif==[]:
    min_positif = min(liste_postif)
    print(min_positif)
else:
    max_negatif = max(liste_negatif)
    valeur_absolue_max_negatif =  -max_negatif
    min_positif = min(liste_postif)
    
    liste_final.append(min_positif)
    liste_final.append(valeur_absolue_max_negatif)

closest_temperature= min(liste_final)

print(closest_temperature)
