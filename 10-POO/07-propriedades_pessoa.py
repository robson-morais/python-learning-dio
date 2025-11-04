class Pessoa:
    def __init__(self, nome, ano):
        self._nome=nome
        self._ano_nascimento=ano

    @property
    def name(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self._ano_nascimento


a = Pessoa("Ana", 2001)
print(a.idade)
