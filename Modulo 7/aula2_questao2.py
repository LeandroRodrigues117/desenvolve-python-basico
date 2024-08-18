def substituir_vogais(frase):
    
    vogais = "aeiouAEIOU"
 
    frase_modificada = ''.join('*' if char in vogais else char for char in frase)
    return frase_modificada

def main():
   
    frase = input("Digite uma frase: ")
   
    frase_substituida = substituir_vogais(frase)
   
    print("Frase com vogais substituídas por '*':", frase_substituida)

if __name__ == "__main__":
    main()