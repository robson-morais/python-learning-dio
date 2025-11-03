from pathlib import Path

ROOT_PATH = Path(__file__).parent

#--> 'with' garante que o arquivo será fechado corretamente após a execução ou interrupção
with open(ROOT_PATH / "bp.txt", "r") as arquivo:
    print("Lendo arquivo aberto...")
    print(arquivo.read())

#--> tratando possíveis excessões:
try:
    with open(ROOT_PATH / "p.txt", "r") as arquivo:
        print("Lendo arquivo aberto...")
        print(arquivo.read())
except IOError as erro:
    print(f"Erro ao abrir arquivo: {erro}")

#--> codificação do arquivo:
try:
    with open(ROOT_PATH / "file-utf-8.txt", "r", encoding='ascii') as arquivo2: #--> o arquivo tem encoding='utf-8'
        print("Lendo arquivo aberto...")
        print(arquivo2.read())
except UnicodeDecodeError as erro:
    print(f"Erro ao abrir arquivo (encoding): {erro}")
