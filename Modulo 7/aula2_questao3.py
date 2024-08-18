import re

def limpar_frase(frase):
    
    frase_limpa = re.sub(r'[^a-zA-Z0-9]', '', frase).lower()
    return frase_limpa

def verificar_palindromo(frase):
    frase_limpa = limpar_frase(frase)
    return frase_limpa == frase_limpa[::-1]

def main():
    while True:
        frase = input("Digite uma frase (ou 'Fim' para encerrar): ")
        
        if frase.lower() == "fim":
            break
        
      
        if verificar_palindromo(frase):
            print("A frase é um palíndromo.")
        else:
            print("A frase não é um palíndromo.")

if __name__ == "__main__":
    main()