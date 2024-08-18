from collections import Counter

def encontrar_anagramas(string, palavra_objetivo):
    
    len_objetivo = len(palavra_objetivo)
    
 
    contador_objetivo = Counter(palavra_objetivo)
    
  
    anagramas = []
    
  
    for i in range(len(string) - len_objetivo + 1):
        substring = string[i:i + len_objetivo]
       
        if Counter(substring) == contador_objetivo:
            anagramas.append(substring)
    
    return anagramas


string = input("Digite a string: ")
palavra_objetivo = input("Digite a palavra objetivo: ")


anagramas = encontrar_anagramas(string, palavra_objetivo)


print(f"Anagramas encontrados: {anagramas}")