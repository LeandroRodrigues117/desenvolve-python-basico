import random

def gerar_lista(tamanho, menor, maior):
    return [random.randint(menor, maior) for _ in range(tamanho)]

def encontrar_intervalo_com_mais_negativos(lista):
    max_negativos = 0
    melhor_inicio = 0
    melhor_fim = 0
    
    for i in range(len(lista)):
        for j in range(i + 1, len(lista) + 1):
            intervalo = lista[i:j]
            negativos_count = sum(1 for x in intervalo if x < 0)
            
            if negativos_count > max_negativos:
                max_negativos = negativos_count
                melhor_inicio = i
                melhor_fim = j
    
    return melhor_inicio, melhor_fim

def main():
   
    lista = gerar_lista(20, -10, 10)
    print("Lista original:")
    print(lista)
    
   
    inicio, fim = encontrar_intervalo_com_mais_negativos(lista)
    
  
    del lista[inicio:fim]
    
 
    print("\nLista após remoção do intervalo com mais números negativos:")
    print(lista)

if __name__ == "__main__":
    main()