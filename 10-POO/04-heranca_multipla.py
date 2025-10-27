class Animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, num_patas, cor_pelo):
        super().__init__(num_patas)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, num_patas, cor_asas):
        super().__init__(num_patas)
        self.cor_asas = cor_asas


class Gato(Mamifero):
    pass


class Onitorrinco(Mamifero, Ave):
    pass

gato = Mamifero(4,"branco")
print(gato)