class Veiculo:
    def __init__(self, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas
    
    def ligar_motor(self):
        print("Ligando o motor")


class Carro(Veiculo):
    pass

class Motocicleta(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, num_rodas, carregado):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas
        self.carregado = carregado



    def esta_carregado(self):
        print(f"{'Sim. Está carregado' if self.carregado else 'Não está carregado'}")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

moto = Motocicleta("Preta", "!@#", 4)
moto.ligar_motor()

caminhao = Caminhao("Branco", "abc-1212", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)

