# # Fonctions questionnaire

# questions = [
#     "Quelle est la capitale de la France ?",
#     "Quelle est la capitale de la Mauritanie ?",
#     "Quelle est la capitale  du Ghana ?",
#     "Quelle est la capitale de l'Espagne ?",
# ]

# capitale = [
#     "Nouakchott",
#     "Accra",
#     "Paris",
#     "Madrid",
#     "Lisbonne",
#     "Lilongwe",
#     "Berlin"
# ]


# choix = [
#     "(a) Madrid",
#     "(b) Paris",
#     "(c) Nouakchott",
#     "(d) Berlin"
# ]

# def questionnaire():
#     for i in range (len(questions)):
#         print(questions[i])
#         for i in range(len(choix)):
#             print(choix[i])
#         reponse=input ("Réponse (a) , (b), (c) ou (d) : ")
#         if i == 0:
        
#         if (reponse == "b" or reponse == "Paris"):
#             print("Bonne réponse !")
#         else:
#             print("Mauvaise réponse !")


# questionnaire()
# def poser_question(question,r1,r2,r3,r4, choix_bonne_reponnse):
#     global score
#     print("score:", score)
#     print("QUESTION")
#     print(" "+ question)

##### Fonction récursives

'''def a(n,limit):
    if n > limit:
        return
    print("n:", n)
    a(n*n ,limit)


a(2,100000)'''

'''def demander_choix_utilisateur(min,max):
    reponse_str = input("Quel est votre choix entre " + str(min) + " et " + str(max) + " : ")
    try:
        reponse_int= int(reponse_str)
        if not min <= reponse_int <= max :
            print("ERREUR: Vous devez rentrer un nombre entre", min, " et ", max)
            return demander_choix_utilisateur(min, max)
        return reponse_int
    except:
        print("ERREUR: Vous devez rentrer un nombre")
        return demander_choix_utilisateur(min, max)

choix= demander_choix_utilisateur(1,4)
print("Choix de l'utilisateur:", choix)'''


'''def afficher_table_multiplication(n):
    for i in range(1,10):
        print (i, "x", n , "=", i*n)


def afficher_table_addiion(n):
    for i in range(1,10):
        print (i, "+", n , "=", i+n)'''

def afficher_table(n, operateur_str, operation_cbk):
    for i in range(1,10):
        print (i, operateur_str, n , "=",  operation_cbk(i,n))


# def mult_callback(a,b):
#     return a*b

# def add_callback(a,b):
#     return a+b

# def pow_callback(a,b):
#     return pow(a,b)

# afficher_table(2,"x",lambda a,b : a*b )
# print()
# afficher_table(2,"x",lambda a,b : a+b )
# print()
# afficher_table(2,"^",lambda a,b : pow(a,b))
# print()

# def somme(*nombres):
#     resultat = 0
#     for n in nombres:
#         resultat += n
#     return 
    
def somme(titre ,**nombres):
    print("TITRE:", titre)
    resultat = 0
    for n in nombres.values():
        resultat += n
    return resultat

print(somme("somme des points",maths= 50, angl=2, esp=54))
