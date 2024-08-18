pares_entre_20_e_50 = [x for x in range(20, 51) if x % 2 == 0]
print(pares_entre_20_e_50)

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrados = [x**2 for x in valores]
print(quadrados)

divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]
print(divisiveis_por_7)

paridade = ['par' if x % 2 == 0 else 'ímpar' for x in range(0, 30, 3)]
print(paridade)