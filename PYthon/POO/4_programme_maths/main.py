import random

NOMBRE_MIN =1
NOMBRE_MAX =10

NOMBRE_QUESTIONS = 4

def poser_question():   
        a = random.randint(NOMBRE_MIN,NOMBRE_MAX)
        b = random.randint(NOMBRE_MIN,NOMBRE_MAX)
        o = random.randint(0,1)

        operateur_str = "+"
        if o == 1:
            operateur_str = "*"

        reponse_str = input(f"Calculez: {a} {operateur_str} {b} = ")
        reponse_int = int(reponse_str)
        calcul = a+b
        if o == 1:
            calcul = a*b
        
        if reponse_int == calcul:
            return True

        if reponse_int == a+b:
    
            return True
             
        return False
    

nb_points = 0
for i in range (0, NOMBRE_QUESTIONS):
    print(f"Question n° {i+1} sur {NOMBRE_QUESTIONS}: ")
    if poser_question():
        print("Reponse correcte")
        nb_points += 1
    else:
        print("Reponse incorrecte")
    print()

print(f"Votre note est : {nb_points} / {NOMBRE_QUESTIONS}")

moyenne = int(NOMBRE_QUESTIONS)/2
if nb_points == 0 :
    print("Revisez vos maths!")
elif nb_points < moyenne:
    print("Peut mieux faire")
elif moyenne < nb_points < NOMBRE_QUESTIONS :
    print("Pas mal")
elif nb_points == NOMBRE_QUESTIONS:
    print("Excellent !")
else:
    print("Tous juste la moyenne!")

print()