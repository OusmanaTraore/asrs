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


t = turtle.Turtle()


# escalier(60,5)

carre(50)
carre(100)
carre(200)


turtle.done()