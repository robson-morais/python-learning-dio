arquivo = open("/home/r0bstark/VSCODE/python-dio-2025/11-manimpulacao-arquivos/teste-w.txt", "w")
arquivo.write("Ecrevendo nesse arquivo")
arquivo.writelines([" Python\nwritex"])
arquivo.close()

arquivo2 = open("/home/r0bstark/VSCODE/python-dio-2025/11-manimpulacao-arquivos/shutil_file_test.txt", "w")
arquivo2.close()