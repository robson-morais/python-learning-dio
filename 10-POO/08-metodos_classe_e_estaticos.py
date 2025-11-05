class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def create_from_bday(cls,ano,mes,dia,nome):
        idade = 2025 - ano
        return cls(nome, idade)
    
    @staticmethod
    def eh_maioridade(idade):
        return idade >= 18
    
    def __str__(self):
        return f'Idade: {self.idade}\nNome: {self.nome}'
    
p = Pessoa.create_from_bday(2003,4,7,"Robson")
print(p)

print(p.eh_maioridade(p.idade))
print(p.eh_maioridade(17))