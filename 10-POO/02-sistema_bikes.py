class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Bzzzz...")

    def parar(self):
        print("Parando")

    def correr(self):
        print("Correndo!")

    #def __str__(self):
     #   return f"""
      #        Informações do produto:
       #       Modelo: {self.modelo},
        #      Ano: {self.ano},
         #     Valor: R$ {self.valor:.2f}
          #    """
    def __str__(self):
        return f"{self.__class__.__name__}:\n {',\n '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


caloi = Bicicleta("Vermelha", "Caloi", 2022, 600)
caloi.buzinar()
caloi.correr()

print(caloi)

#também:
Bicicleta.correr(caloi)

#os atributos são públicos por padrão; logo, são acessísveis
print(caloi.cor)
