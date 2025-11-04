#CSV = Comma Separated Values
import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent


# try:
#     with open(ROOT_PATH / "usuarios.csv", "w", encoding="utf-8") as arquivo:
#         escritor = csv.writer(arquivo)
#         escritor.writerow(['id', 'nome'])
#         escritor.writerow(['1', 'Maria'])
#         escritor.writerow(['2', 'Joao'])

# except IOError as exc:
#     print("Erro")

try:
    with open(ROOT_PATH / "usuarios.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row[0], row[1])

except IOError as exc:
    print("Erro")