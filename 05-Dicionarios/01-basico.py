#pares ordenados de chave-valor separados por vírgula
#--> objeto = {"chave":"valor", "chave":"valor"}
#ainda --> objeto = dict(chave="valor", chave="valor")

pessoa = {"nome":"Robson", "idade":22}
pessoa = dict(nome="Robson", idade=22)

pessoa["telefone"] = "3322-4422" #--> adiciona um valor ao dicionario {"nome":"Robson", "idade":22, "telefone":"3322-4422"}

print(pessoa)

#buscando valores
pessoa["nome"] #Robson
pessoa["telefone"] #3322...

#alterano valores
pessoa["nome"] = "Maria"
pessoa["telefone"] = "1234-5678"

print(pessoa)