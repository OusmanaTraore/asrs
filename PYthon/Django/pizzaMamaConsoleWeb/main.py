import requests
import json

url = "https://yous-pizzamamadjango.herokuapp.com/api/GetPizzas"

# recuperation des données de l'API
# sérialisation : format json
data= requests.get(url)
# print(data.text)

# désérialisation : format text
pizzas = json.loads(data.text)
# print(pizzas)
print("liste des pizzas")

for pizzaModel in pizzas:
    pizza = pizzaModel['fields']
    print(pizza['nom'] + " : " + str(pizza['prix']))