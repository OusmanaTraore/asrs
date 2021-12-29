
# noms = []

# while True:
#     nom=input("Nom de la personne : ")
#     if nom == "":
#         break
#     noms.append(nom)

# print()
# print("Nom des personnes:")
# noms.sort()
# for nom in noms:
#     print(" " + nom)

# Liste Algo : valeur la plus petite

chauffeur = ["Marc", "Jean", "Patrick","Cédric", "Sébastien", "Antoine", "Aimé"]
distance_chauffeur_km = [1.5,2.2,0.4, 0.9,7.1,1.1,2.2]

index_min=0
distance_min= distance_chauffeur_km[0] 

for i in range(len(distance_chauffeur_km)):
    distance = distance_chauffeur_km[i]
    if distance < distance_min:
        distance_min = distance
        index_min= i

print("Distance minimale: ", distance_min , "km")
print("index minimal: ", index_min)
print("Nom du  chauffeur : ", chauffeur[index_min])