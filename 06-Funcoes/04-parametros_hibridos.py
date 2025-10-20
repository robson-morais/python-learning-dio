#def function (pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2)

#por posicao ou por keywords --> os argumentos devem seguir uma mesma ordem no lado em que estão -- um lado nao precisa estar igual ao outro
def criar_carro(modelo, marca, ano, /, placa, motor, combustivel):
    print(modelo, marca, ano, placa, motor, combustivel)


criar_carro("Uno", "Fiat", "1998", placa="ABC123", motor=1.0, combustivel="Gasolina")

#por keyword only:
def criar_phone(*,modelo, marca, ano):
    print(modelo, marca, ano)

criar_phone(modelo="iPhone 17 Pro Max", ano=2025, marca="Apple" )

#por posicao E keywords:

def criar_carro2(modelo, marca, ano, /,*, motor, placa):
    print(modelo, marca, ano, motor, placa)

criar_carro2("palio", "fiat", 1999, motor=1.0, placa="ABC123")