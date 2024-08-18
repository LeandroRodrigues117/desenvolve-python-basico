def main():
    print("Digite uma quantidade indefinida de números inteiros. Digite 'sair' para encerrar.")
    
    numeros = []
    
    while True:
        entrada = input("Digite um número inteiro (ou 'sair' para terminar): ")
        if entrada.lower() == 'sair':
            if len(numeros) < 4:
                print("Você deve inserir pelo menos 4 números.")
                continue
            else:
                break
        
        try:
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

 
    print("\nLista original:")
    print(numeros)
    
   
    print("\nOs 3 primeiros elementos:")
    print(numeros[:3])
    
   
    print("\nOs 2 últimos elementos:")
    print(numeros[-2:])

 
    print("\nLista invertida:")
    print(numeros[::-1])
    
 
    print("\nElementos de índice par:")
    print(numeros[::2])
  
    print("\nElementos de índice ímpar:")
    print(numeros[1::2])

if __name__ == "__main__":
    main()
