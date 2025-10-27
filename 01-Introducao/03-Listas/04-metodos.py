#.copy() --> faz uma cópia da lista
letras = ["d", "a", "b", "c", "a", "e"]
l1 = letras.copy()

print(letras)
print(l1)

#.count() --> conta a frequencia de um elemento na lista
letras.count("a") #2
letras.count("b") #1

#.len() --> indica o tamanho (lenght) da lista
len(letras)

#.extend([]) --> Diferente do .append(x) que só adiciona um parâmetro por vez na lista, este método merge uma lista inteira com a lista original no final
letras.extend(["e", "i"]) 

#.index() --> indica a primeira posição do item na lista
print(letras.index("a"))

#.pop() --> por padrão, os itens são adicionados no padrão pilha (LIFO)
letras.pop() #e

#.remove() --> remove qualquer item da lista
letras.remove("d")

#.reverse funciona como o modo de fatiamento "letras[::-1]""
letras.reverse()

#.sort
print(sorted(letras))
print(letras.sort()) #--> ordem alfabética

letras.sort(reverse = True)  #--> ordem alfabética reversa

letras.sort(key = lambda x: len(x)) #--> ordem alfabetica crescente (quantidade de caracteres)
letras.sort(key = lambda x: len(x), reverse = True) #--> ordem alfabética decrescente

