import funcoes_conta

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def entrar():
    global saldo, limite, extrato, numero_saques, LIMITE_SAQUES
    menu_conta = f"""
    Bem-vindo(a), 
    [a] Depositar
    [b] Sacar
    [c] Extrato
    [d] Sair
    => """
    
    while True:
        opcao = input(menu_conta)
        
        if opcao == "a":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = funcoes_conta.fazer_deposito(valor,saldo,extrato)

        elif opcao == "b":
            saldo, extrato, numero_saques = funcoes_conta.fazer_saque(saldo=saldo, extrato=extrato, limite=limite, LIMITE_SAQUES=LIMITE_SAQUES, numero_saques=numero_saques)
    
        elif opcao == "c":
            funcoes_conta.conferir_extrato(saldo,extrato=extrato)
    
        elif opcao == "d":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")