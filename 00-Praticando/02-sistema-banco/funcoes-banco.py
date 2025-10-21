#saque
#deposito
#extrato
#cadastrar usuarios
#cadastrar contas
def criar_cliente(cpf,nome,data_nascimento,endereco):
    usuario = [cpf,nome,data_nascimento,endereco]
    return usuario

id = 0 #contador para o numero das contas
def criar_conta_corrente(usuario_cpf):
    AGENCIA = "0001"
    global id
    id+=1
    conta = [id,AGENCIA,usuario_cpf]
    return conta








