def formatar_mensagem(texto):
    # Remove espaços extras do início e do fim da string
    texto = " ".join(texto.lower().strip().split())

    return texto

# Lê a mensagem enviada ao robô via input padrão
entrada = input()  # Tipo de dado esperado: str

# Chama a função formatar_mensagem (você irá implementar a lógica)
saida = formatar_mensagem(entrada)

# Exibe a mensagem padronizada
print(saida)