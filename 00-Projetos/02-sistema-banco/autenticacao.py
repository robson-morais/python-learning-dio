
def cpf_vinculo(cpf, usuarios):
    vinculado = False
    for usuario in usuarios:
        if usuario[0] == cpf:
            vinculado = True
    return vinculado

        
def vinculo_conta(cpf, contas):
    tem_conta = False
    for conta in contas:
        if cpf == conta[0]:
            tem_conta = True
    return tem_conta


def aut_conta_senha(senha,cpf,usuarios,contas):
    autorizacao = False
    if cpf_vinculo(cpf,usuarios) and vinculo_conta(cpf, contas):
        for conta in contas:
            if conta[3] == senha:
                print("Acesso liberado!")
                autorizacao = True
    return autorizacao       



