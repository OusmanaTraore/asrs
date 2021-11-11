import turtle

# Definition de fonction d'escalier
def escalier(taille, nb):

    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        taille -= 10
    t.forward(taille)

def carre(taille):
    for i in range(0,4):
        t.forward(taille)
        t.left(90)


def carres(taille_depart, nb):
    for  i in range (1, nb+1):
        taille =  i* taille_depart
        carre(taille)


t = turtle.Turtle()


# escalier(60,5)


carres(10,10)


turtle.done()