import random
from collections import Counter


lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]


interseccao = list(set(lista1) & set(lista2))


interseccao_ordenada = sorted(interseccao)


contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)


print("Lista 1:")
print(lista1)
print("Lista 2:")
print(lista2)


print("Lista interseccao ordenada:")
print(interseccao_ordenada)


print("Quantidade de vezes que cada elemento aparece em Lista 1:")
for item, count in contagem_lista1.items():
    print(f"Valor {item}: {count} vez(es)")

print("Quantidade de vezes que cada elemento aparece em Lista 2:")
for item, count in contagem_lista2.items():
    print(f"Valor {item}: {count} vez(es)")