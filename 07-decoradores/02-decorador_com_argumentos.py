#*args e **kwargs para usar funcoes com mais de um parametro

def meu_decorador2(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes:")
        funcao(*args, **kwargs)
        print("já foi feito") #*aqui o print acontece, mas nao é um retorno, e se a funcao tivesse retorno, nao aconteceria nada(None), pois a subfuncao nao esta dando nenhum retorno à funcão pai.
    return envelope

@meu_decorador2
def ola_mundo(nome):
    print(f"Olá, mundo, {nome}")
    return nome.upper() #se  funcao tem retorno, ele é ignorado *

resultado = ola_mundo("Robson")
print(resultado)