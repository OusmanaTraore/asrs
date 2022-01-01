class Personne:
    def __init__(self, nom,age):
        self.nom=nom
        self.age=age
        # self.amis=amis

    def AfificherInfos(self):
        print(f"je m'appelle  {self.nom}, j'ai {self.age} ans")

    def __str__(self):
        return "STR"
    
    def __repr__(self):
        return __class__.__name__ + " " + str(self.__dict__)



personne1 = Personne("Jean", 20)
personne1.AfificherInfos()

print(personne1)