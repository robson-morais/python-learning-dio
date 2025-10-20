def show_message():
    print("hello, world!")
show_message()


def show_greetings(name):
    print(f"Welcome to Python 3.0.8, {name}!")
name = "Diias"
show_greetings(name)


def soma(a,b):
    print (a + b)
soma(3,5)


def suce_ante (numero):
    sucessor = numero +1
    antecessor = numero -1
    return antecessor, sucessor
print(suce_ante(4))


def salvar_smartphone(marca,modelo,ano):
    print(f"Smartphone salvo! {marca}{modelo}")