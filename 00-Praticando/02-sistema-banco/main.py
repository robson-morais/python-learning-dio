import funcoes_conta
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = funcoes_conta.fazer_deposito(valor,saldo,extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = funcoes_conta.fazer_saque(saldo=saldo, extrato=extrato, limite=limite, LIMITE_SAQUES=LIMITE_SAQUES, numero_saques=numero_saques)
    
    elif opcao == "e":
        funcoes_conta.conferir_extrato(saldo,extrato=extrato)
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")