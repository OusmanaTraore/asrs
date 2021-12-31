
class Pizza:
    def __init__(self,nom , prix,ingredients, vegetarienne=False):
        self.nom =  nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne=vegetarienne
    
    def Afficher(self):
        veg_str=""
        if self.vegetarienne:
            veg_str = " - VEGETARIENNE"
        print(f"PIZZA {self.nom} : {self.prix}£" + veg_str)
        print(", ".join(self.ingredients))
        print()
       

class PizzaPersonnalisee(Pizza):
    PRIX_DE_BASE = 7 
    PRIX_PAR_INNGREDIENT = 1.2
    dernier_numero = 0 

    def __init__(self):
        PizzaPersonnalisee.dernier_numero += 1
        self.numero = PizzaPersonnalisee.dernier_numero
        super().__init__("Personnalisée " + str(self.numero), 0,[])
        self.demander_ingredients_utilisateur()
        self.calculer_le_prix()
    
    def demander_ingredients_utilisateur(self):
        print()
        print(f"Ingredients pour la pizza personnalisée {self.numero}")
        while True:
            ingredient = input("Ajouter un ingrédient (ou ENTRER pour terminer): ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingrédient(s) : {', '.join(self.ingredients)}")

    def calculer_le_prix(self):
        self.prix = self.PRIX_DE_BASE + len(self.ingredients)*self.PRIX_PAR_INNGREDIENT

pizzas =[
     Pizza("4 fromages" , 8.5, ("brie", "emmental", "compté","parmesan"),True),
     Pizza("orientale" , 9.5, ("merguez", "olive", "fromage","oignon")),
     Pizza("merguez" , 12, ("merguez", "tomate")),
     Pizza("thon" , 10.5, ("thon", "oignon", "sauce")),
     Pizza("Végétarienne" , 7, ("salade","fromage"),True),
     PizzaPersonnalisee(),
     PizzaPersonnalisee()
     
     ]

# def tri(e):
#     return len(e.ingredients)

# pizzas.sort(key=tri)

for pizza in pizzas:
    # if not pizza.vegetarienne:
    pizza.Afficher()