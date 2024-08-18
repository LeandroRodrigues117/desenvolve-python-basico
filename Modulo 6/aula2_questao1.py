import random


lista_original = [random.randint(-100, 100) for _ in range(20)]

lista_ordenada = sorted(lista_original)


print("Lista ordenada:")
print(lista_ordenada)


print("Lista original:")
print(lista_original)


indice_maior = lista_original.index(max(lista_original))
print("Índice do maior valor:", indice_maior)


indice_menor = lista_original.index(min(lista_original))
print("Índice do menor valor:", indice_menor)