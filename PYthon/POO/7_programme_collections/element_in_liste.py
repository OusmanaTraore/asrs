def element_dans_liste(e,l):
    l_lower = [el.lower() for el in l]
    return e.lower() in l_lower

noms =["Sophie","Jean", "Martin", "Zoe", ]

if element_dans_liste("jean", noms):
    print("Element trouvé")
else:
    print("Element non  trouvé")