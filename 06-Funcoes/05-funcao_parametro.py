def somar(a, b):
    return a+b

def exibir_resultado(a, b, somar):
    resultado = somar(a,b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(1, 4, somar)