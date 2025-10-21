import autenticacao
#cadastrar usuarios
#cadastrar contas
def cadastrar_cliente(cpf,usuarios,contas):
    cadastro = False
    if (autenticacao.cpf_vinculo(cpf, usuarios)):
        print("Esse CPF já está cadastrado.")

    else:
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento (DDMMAAAA): ")
        ende1 = input("(Endereço)\nLogradouro: ")
        ende2 = input("Bairro: ")
        ende3 = input("Cidade e UF (Ex.: João Pessoa-PB): ")
        endereco = ende1 + "," + ende2 + "," + ende3

        cliente = [cpf,nome,data_nascimento,endereco]
        conta = criar_conta_corrente(cpf)
        usuarios.append(cliente)
        contas.append(conta)
        cadastro = True
        
    return cadastro

id = 0 #contador para o numero das contas
def criar_conta_corrente(usuario_cpf):
    AGENCIA = "0001"
    global id
    id+=1
    senha = input("Escolha uma senha de 4 dígitos: ")
    conta = [usuario_cpf,AGENCIA,id,senha]
    print(conta)
    return conta

