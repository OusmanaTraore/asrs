import os.path

if not os.path.exists("rep"):
    os.mkdir("rep") # création de repertoire
    # os.rmdir("rep") supprimer un répertoire

filename =os.path.join("rep", "mon_fichier.txt")
if os.path.exists(filename):
    print(filename ,'existe')
    f = open(filename,'r')
    texte= f.read()
    print(texte)
    f.close
else:
    print(filename, "n'existe pas")
    f = open(filename,'w')  # création de fichier
    # os.remove(filename) supprimer un fichier