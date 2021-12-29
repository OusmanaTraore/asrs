# def tri_personalise(e):
#     return len(e)

def afficher(collection, n_premiers_elements=-1):
    # "------LISTES DES PIZZAS (4)--------"
    # afficher les pizzas 1 pizzas par ligne
    # collection.sort(reverse=True, key=tri_personalise)
    c= collection
    if not n_premiers_elements == -1:
        c = collection[:n_premiers_elements]
    
    nbre_pizzas= len(c)
    if nbre_pizzas == 0:
        print("AUCUNE PIZZA")
        return

    print(f"------LISTES DES PIZZAS ({nbre_pizzas})--------")
    for i in c:
        print(i)
    print()
    print("Première Pizza: " + c[0])
    print("Dernière Pizza: " + c[-1])


def ajouter_pizza_utilisateur(collection):
    p = input("Pizza à ajouter: ")
    if p.lower() in collection:
        print("ERREUR : Cette pizza existe déjà !")
    else:
        collection.append(p)

pizzas = ["4 fromages", "végétarienne", "hawai", "orientale"]

vide=()
ajouter_pizza_utilisateur(pizzas)
afficher(pizzas,4)