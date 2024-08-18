import emoji

def listar_emojis():
    emojis = emoji.EMOJI_DATA
    print("Lista de emojis disponíveis:")
    for code, data in emojis.items():
        print(f"{code}: {data['en']}")

def emojizar_frase(frase_codificada):
    # Decodifica a frase codificada em emojis
    frase_emojizada = emoji.emojize(frase_codificada, use_aliases=True)
    return frase_emojizada

def main():
    listar_emojis()
    
    frase_codificada = input()
    
    frase_emojizada = emojizar_frase(frase_codificada)
    print("Frase emojizada:", frase_emojizada)

    main ()