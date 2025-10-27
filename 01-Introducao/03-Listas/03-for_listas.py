numeros = [1, 2, 5, 3, 0, 7, 2, 5, 9, 6, 7]
pares = []

for i in numeros:
    if i%2 == 0:
        pares.append(i)
print(numeros)
print(pares)

impares = [i for i in numeros if i%2 != 0]
maiores_que_5 = [a for a in numeros if a>5]
menores_que_5 = [b for b in numeros if b < 5]

print(impares)
print(f"""
      Números ímpares: {impares}, 
      números pares: {pares}
      """)



