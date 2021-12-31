#Join
noms =[ "Join","Eric","Christophe","Zoé"]


# noms_join = "+".join(noms)

# print(noms_join)

# # Split
# a = "Paul-Marc-Eric"

# a_split = a.split("-")
# print(a_split)

# index, find ,count

# element_cherche = "Martin"
# nb_occurences = noms.count(element_cherche)
# print("nb_occurences", nb_occurences)
# if nb_occurences > 0:
#     index_occurence =0 
#     for i in range(nb_occurences):
#         index_occurence = noms.index(element_cherche, index_occurence)
#         print(element_cherche, "trouvé à ", index_occurence)
#         index_occurence +=1
# else:
#     print("element n'est pass dans la collection")


longeurs_noms = [len(nom) if len(noms) < 10 else 0  for nom in noms]
noms_avec_e= [nom for nom in noms if "e" in nom]

# a= [i for i in range(11)]

# print(longeurs_noms)

def chaine_contient_chiffre(chaine):
    return any([c.isdigit() for c in chaine])


nom =input('Quel est ton nom ?')
if nom == "":
    print('Le nom est vide')
elif chaine_contient_chiffre(nom):
    print("Ce nom est invalide, il ne doit pas contenir de chiffres")
else:
    print("Bonjour " + nom)