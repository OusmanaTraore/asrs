import json


personne = {
    "nom": "Paul",
    "age": 25,
    "amis":["Sophie", "Marc","Jean"]
}

# ====Conversion au format JSON ======
personne_json= json.dumps(personne)
print("JSON:" + personne_json)

f =open("fichier_json.txt", "w")
f.write(personne_json)
f.close()
#=====================================

# ====Conversion au format txt ======
f =open("fichier_json.txt", "r")
donnees_json=f.read()
f.close

personne= json.loads(donnees_json)
print("NOM:" + personne["nom"])
#=====================================