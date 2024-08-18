def receber_lista(nome_lista):
    
    while True:
        try:
            entrada = input(f"Digite os números para a {nome_lista}, separados por espaço: ")
            lista = list(map(int, entrada.split()))
            return lista
        except ValueError:
            print("Entrada inválida. Por favor, insira apenas números separados por espaço.")

def combinar_listas(lista1, lista2):
    
    combinada = []
    tamanho_minimo = min(len(lista1), len(lista2))
    
   
    for i in range(tamanho_minimo):
        combinada.append(lista1[i])
        combinada.append(lista2[i])
    
    if len(lista1) > len(lista2):
        combinada.extend(lista1[tamanho_minimo:])
    else:
        combinada.extend(lista2[tamanho_minimo:])
    
    return combinada


lista1 = receber_lista("primeira lista")
lista2 = receber_lista("segunda lista")


lista_combinada = combinar_listas(lista1, lista2)


print("Primeira lista:")
print(lista1)
print("Segunda lista:")
print(lista2)
print("Lista combinada:")
print(lista_combinada)