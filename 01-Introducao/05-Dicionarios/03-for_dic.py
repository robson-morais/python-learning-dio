contatos = {
    "robson@gmail.com": {"nome": "robson", "idade": 22},
    "morais@outlook.com": {"nome": "yeat", "idade": 20},
    "alice@spotify.org": {"nome": "alice", "idade": 33},
    "steb@email.com": {"nome": "steb", "idade": 44},
    "luna@python.dev": {"nome": "luna", "idade": 27}
}

for chave, valor in contatos.items():
    print(chave,valor)

for chave in contatos:
    print(chave, contatos[chave])