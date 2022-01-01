class Personne:
    TYPE = "Humain"
    def __init__(self, nom):
        self.nom=nom
        # self.age=age
        # self.amis=amis

    def AfificherInfos(self):
        print(f"je m'appelle  {self.formater_chaine(self.nom)} - " + self.TYPE)

    @staticmethod
    def formater_chaine(a):
        return a[0].upper() + a[1:].lower() 
    
    @classmethod
    def method_de_classe(cls):
        print("Methode de classe : " + cls.TYPE)



personne1 = Personne("Jean", 20)
personne1.AfificherInfos()

print(Personne.formater_chaine("toto"))

Personne.method_de_classe()