from pathlib import Path

#--> com arquivos
try:
    file = open("file.txt", "r")
except FileNotFoundError as a:
    print("Aquivo não encontrado")
    print(a)

#--> arquivo vs diretorio
ROOT_PATH = Path(__file__).parent
try:
    arquivo = open(ROOT_PATH / "novo-diretorio")
except IsADirectoryError as er:
    print(f"Não foi possivel abrir o arquivo: {er}")