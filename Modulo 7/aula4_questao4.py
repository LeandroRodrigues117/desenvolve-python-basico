import random


def carregar_palavras(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        palavras = [linha.strip() for linha in arquivo]
    return palavras


def carregar_estagios(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        estagios = [linha.strip() for linha in arquivo]
    return estagios


def imprime_enforcado(num_erros, estagios):
    if num_erros < len(estagios):
        print(estagios[num_erros])
    else:
        print("Número de erros excede o número de estágios disponíveis.")


def jogar_forca():
    palavras = carregar_palavras("gabarito_forca.txt")
    estagios = carregar_estagios("gabarito_enforcado.txt")
    
    palavra = random.choice(palavras).upper()
    letras_adivinhadas = set()
    tentativas = 6
    erros = 0
    
    progresso = ['_' for _ in palavra]

    print("Bem-vindo ao jogo da forca!")
    
    while tentativas > 0:
        print("\nPalavra: " + " ".join(progresso))
        letra = input("Digite uma letra: ").upper()

        if letra in letras_adivinhadas:
            print("Você já tentou essa letra.")
            continue
        
        letras_adivinhadas.add(letra)
        
        if letra in palavra:
            for i, char in enumerate(palavra):
                if char == letra:
                    progresso[i] = letra
        else:
            erros += 1
            imprime_enforcado(erros, estagios)
            tentativas -= 1
            print(f"Erros restantes: {tentativas}")
        
        if "_" not in progresso:
            print("\nParabéns! Você adivinhou a palavra:", palavra)
            break
    else:
        print("\nGame over! A palavra era:", palavra)


if __name__ == "__main__":
    jogar_forca()