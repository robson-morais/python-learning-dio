def salvar_modelo(marca,modelo,ano):
    print(f"Smartphone inserido com sucesso:\n{marca}\n{modelo}\n{ano}\n\n")

salvar_modelo(marca="Samsung",modelo="Galaxy S25 Edge",ano=2025)
salvar_modelo("Apple","iPhone 5",2016)
salvar_modelo(**{"marca":"Motorola", "modelo":"Moto Edge 60", "ano":2025})
