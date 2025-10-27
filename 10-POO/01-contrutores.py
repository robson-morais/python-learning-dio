class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print("Auau")

    def dormir(self):
        self.acordado = False
        print("Zzzz...")

#Instanciando objeto:

cao_1 = Cachorro("mel", "amarela", True)
cao_2 = Cachorro("rick", "preto", False)

cao_1.latir()
cao_2.latir()
    
