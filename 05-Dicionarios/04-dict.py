contatos = {
    "robson@gmail.com": {"nome": "robson", "idade": 22},
    "morais@outlook.com": {"nome": "yeat", "idade": 20},
    "alice@spotify.org": {"nome": "alice", "idade": 33},
    "steb@email.com": {"nome": "steb", "idade": 44},
    "luna@python.dev": {"nome": "luna", "idade": 27}
} 

novo_dicionario = contatos.copy() #--> cria um outro dicionário independente

#.get()
contatos.get("robson@gmail.com") #--> se não houver valor, o retorno é none
contatos.get("robson@gmail.com",{}) #--> se não houver valor, o retorno é "{}" (que pode ser uma mensagem)


#.pop() --> remove o valor da chave
contatos.pop("robson@gmail.com") #--> remove o valor e o retorna
contatos.pop("robson@gmail.com", {}) #--> remove o valor e retorna "{}"

contatos.popitem() # --> remove as chaves e os valores  


#dict.fromkeys([]) determina um dicionário a partir de chaves passadas como parâmetro
chaves = ["sexo", "altura"]
dicionario = dict.fromkeys(chaves)#--> com valores vazios (none)

chaves2 = ["sexo", "altura"]
dicionario2 = dict.fromkeys(chaves2, "a definir")#--> adiciona às chaves o valor ("a definir")


#.setdefault()
contatos.setdefault("nome", "Abel") #--> é ignorado pois "nome" já tem um valor
contatos.setdefault("id", 22) #--> adiciona ao final


#.update()
contatos.update({"robson@gmail.com": {"nome":"novo nome"}}) #substitui o valor anterior pelos novos valores
contatos.update({"rsn@gmail.com": {"nome": "rsn", "idade":33}}) #se este valor não existia antes, agora ele existe


#retornar dados:
contatos.values() #--> retorna os valores de todas as chaves
contatos.keys() #--> retorna as chaves 


#in --> para verificar se uma chave está presente no dicionário
"robson@gmail.com" in contatos #--> True
"maria@gmail.com" in contatos #--> False
print(contatos)
print("nome" in contatos["robson@gmail.com"]) #--> True
print("valores" in contatos["morais@outlook.com"]) #--> false


#del --> para deletar valores
#del contatos ["luna@python.dev"]["idade"]
del contatos ["robson@gmail.com"]


print(contatos)
contatos.clear() #--> limpa todos os valores do dicionário