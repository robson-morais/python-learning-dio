arquivo = open("/home/r0bstark/VSCODE/python-dio-2025/11-manimpulacao-arquivos/teste-r.txt", "r")

#print(arquivo.read()) #-> imprime o arquivo todo de uma vez

print(arquivo.readline()) #-> imprime uma linha do arquivo por vez

for linha in arquivo.readline(): #percorre uma linha
    print(linha)

print(arquivo.readlines()) #-> Retorna uma lista com todas as linhas do arquivo

for linha in arquivo.readlines(): #-> percorre a lista com todas as linhas
    print(linha)

for linha in arquivo:
    print(linha)

while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()
