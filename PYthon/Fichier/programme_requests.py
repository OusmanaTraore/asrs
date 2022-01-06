import requests
import json

reponse = requests.get("https://codeavecjonathan.com/res/pizzas1.json")
if reponse.status_code == 200:
    reponse.encoding ="utf-8"
    print(reponse.text)
    pizzas = json.loads(reponse.text)
    print("Nombre de pizzas: ", len(pizzas))
else:
    print("ERREUR code: " +  str(reponse.status_code))

reponse = requests.get("https://codeavecjonathan.com/res/exemple.html")
if reponse.status_code == 200:
    reponse.encoding ="utf-8"
    print(reponse.text)
else:
    print("ERREUR code: " +  str(reponse.status_code))



reponse = requests.get("https://codeavecjonathan.com/res/papillon.jpg")
if reponse.status_code == 200:
    f = open("papillon.jpg","wb")
    f.write(reponse.content)
    f.close()
    print("Ecriture terminée")
else:
    print("ERREUR code: " +  str(reponse.status_code))    