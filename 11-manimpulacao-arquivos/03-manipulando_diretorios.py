import os
import shutil 
from pathlib import Path

ROOT_PATH = Path(__file__).parent #-> Retorna o diretorio pai deste arquivo

os.mkdir(ROOT_PATH / "novo-diretorio") #-> cria um diretorio na pasta pai. A "/" garante a formatação do caminho independente de sistema operacional

arquivo = open(ROOT_PATH / "file_created.txt", "w") #-> cria um arquivo na pasta passada como parâmetro (nesse caso, a pasta pai)

os.rename(ROOT_PATH / "file_created.txt", ROOT_PATH / "modified_file.txt") 

os.remove(ROOT_PATH / "modified_file.txt") 

#===========================

shutil.move(ROOT_PATH / "shutil_file_test.txt", ROOT_PATH / "novo-diretorio") #-> movendo um arquivo para um diretorio

#os.mkdir("novo-diretorio")
#file = open("teste-r.txt")

#===============practicing more
os.mkdir(ROOT_PATH / "boas-praticas")