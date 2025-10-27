def identificar_categoria_gadget(codigo):

    letra1 = codigo[0].lower()
    categoria = ""
    
    if letra1 == "t":
      categoria = "tablet"
      
    elif letra1 == "p":
      categoria = "phone"
      
    elif letra1 == "n":
      categoria = "notebook"
    
    else:
      categoria = "unknown"
      
    return categoria
# Leitura da entrada (espera-se uma string representando o código do gadget)
codigo_gadget = input().strip()

# Chamada da função e saída do resultado
categoria = identificar_categoria_gadget(codigo_gadget)

print(categoria)  # Deve imprimir uma das categorias ou 'unknown'