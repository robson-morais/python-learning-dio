import functools
#antes a subfuncao nao dava retorno para a funcao, entao, por padrao, retornava none. Mas a subfuncao pode retornar uma variável
def meu_decorador2(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):

        print("faz algo antes:")
        retorno = funcao(*args, **kwargs)
        print("já foi feito")

        return retorno
    return envelope

@meu_decorador2
def ola_mundo(nome):
    print(f"Olá, mundo, {nome}")
    return nome.upper()

a = ola_mundo("Robson")
print(ola_mundo.__name__) #antes seria 'envelope'