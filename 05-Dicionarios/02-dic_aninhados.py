#objeto={ "chave_A": {"subchave_a":"subvalor_a", "subvalor_b":"subvalor_b"}
#         "chave_B": {"subchave_b":"subvalor_b", "subchave_c":"subvalor_b"}        
#       }

contatos = {
    "robson@gmail.com" : {"nome":"robson", "idade":22},
    "morais@outlook.com": {"nome":"yeat", "idade":20}
}

print(contatos)

#acessando um dado
contatos["morais@outlook.com"]["idade"]

#adicionando um dado no dicionário
contatos["alice@spotify.org"] = {"nome":"alice", "idade":33}

print(contatos)
