import time
import sys

chaine = "Il s'agit d'un test"


def afficher(char:str):
    text2=""
    for i in char:
        # print(text) 
        # sys.stdout.write(text)
        # sys.stdout.flush()
    # sys.stdout.write(len(text))
    # sys.stdout.flush()
        # print(i)
        text2 +=i
        time.sleep(0.5)
    print(text2)
    


afficher(chaine)