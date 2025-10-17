#.copy() --> faz uma cópia da lista
letras = ["a", "b", "c", "a"]
l1 = letras.copy()

print(letras)
print(l1)

#.count() --> conta a frequencia de um elemento na lista
letras.count("a") #2
letras.count("b") #1

#.extend([])
letras.extend(["e", "i"]) # Diferente do .append(x) que só passa x, este método merge uma lista inteira com a lista original no final

#.index() --> indica a primeira posição do item na lista
print(letras.index("a"))