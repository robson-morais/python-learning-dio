#Maiúsculas e Minúsculas
curso = "pYthoN"
print(curso)
print(curso.upper())
print(curso.lower())
print(curso.capitalize())

#Espacos em branco
curso1 = "  Python  "
print(curso1)
print(curso1.strip())
print(curso1.lstrip())
print(curso1.rstrip())

#Junções e centralização
curso2 = "Python"
print(curso2.center(12, "*")) #A string terá 12 caracteres, o texto da variável e o restante "*"
print("*".join(curso2)) #Adiciona o caractere passado como divisor entre os caracteres da string da variável
