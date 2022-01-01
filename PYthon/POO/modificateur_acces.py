# class Personne:
#     def __init__(self, nom):
#         #private
#         self.__nom=nom

#     def AfificherInfos(self):
#         print(f"je m'appelle  {self.__nom}  ")

 


# personne1 = Personne("Jean")
# personne1.nom = "Toto"

# personne1.AfificherInfos()

# print(personne1.__dict__)

class Personne():
    A = ""
    def __init__(self, nom):
        self.nom = nom
 
    def f(self):
      print(Personne.A)
      print(self.A)
      print(self.nom)
      print("---")

Personne.A = "1"
a = Personne("toto")
a.A = "1"

Personne.A = "2"
b = Personne("titi")
b.A = "2"
 
Personne.A = "3"
a.f()
 
Personne.A = "4"
b.f()