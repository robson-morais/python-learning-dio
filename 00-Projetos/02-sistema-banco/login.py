import funcoes_banco
import conta_corrente
import autenticacao

usuarios = []
contas = []

menu_login = """
Bem-vindo(a)
[a] Entrar
[b] Criar Conta Corrente 
[c] Sair

=> 
"""
while True:
    opcao = input(menu_login)
    
    if opcao == "a":
        cpf = input("CPF: ")
        if (autenticacao.cpf_vinculo(cpf,usuarios)):
            print("Usuário válido")
            senha = input("Senha: ")
            if (autenticacao.aut_conta_senha(senha,cpf,usuarios,contas)):
                conta_corrente.entrar()
            else:
                print("Senha incorreta. Tente novamente.")
        else:
            print("Usuário inválido")


    elif opcao == "b":
        cpf = input("CPF: ")
        if (funcoes_banco.cadastrar_cliente(cpf,usuarios, contas)):
            conta_corrente.entrar()


    elif opcao == "c":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")