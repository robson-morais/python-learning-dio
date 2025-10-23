def calculadora(operacao):
    def soma(a,b):
        return a + b
    def sub(a,b):
        return a - b
    def multi(a,b):
        return a * b
    def div(a,b):
        return a / b
    
    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return multi
        case "/":
            return div

print(calculadora("*")(2,4))
retorno = calculadora("+")(1,9)


def meu_decorador(funcao):
    def envelope():
        print("Antes")
        funcao()
        print("Depois")
    return envelope

@meu_decorador
def funcao():
    print("[Sou a funcao principal]")

funcao()

def duplicar(func):

    def envelope():
        print("faz algo antes de executar")
        func()
        print("faz algo depois de executar")

    return envelope

@duplicar
def aprender():
    print("Estou aprendendo...")

aprender()

