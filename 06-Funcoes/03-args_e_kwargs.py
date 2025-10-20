#recebe os métodos como tupla e dicionário respectivamente

#nesse caso, o nome das variáveis não importa (desde que sejam referenciados corretamente):
def exibir_poema(data,*args,**kwargs):
    texto = "\n".join(args) 
    
    #**kwargs indica que foi passado um dicionário como parâmetro
    #autor="lebrowski", ano=1991
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave,valor in kwargs.items()])

    mensagem = f"{data}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Sunday, 19 of October of 2025","Line 1","Line 2","Line 3", autor="Unknown",ano=1991)
