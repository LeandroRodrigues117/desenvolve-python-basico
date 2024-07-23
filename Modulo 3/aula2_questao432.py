def validar_ficha_personagem(classe, pontos_forca, pontos_magia):
    if classe == "guerreiro":
        return pontos_forca >= 15 and pontos_magia <= 10
    elif classe == "mago":
        return pontos_forca <= 10 and pontos_magia >= 15
    elif classe == "arqueiro":
        return pontos_forca > 5 and pontos_magia > 5 and pontos_forca <= 15 and pontos_magia <= 15
    else:
        return False  # Se a classe fornecida não for uma das válidas

# Solicitar entrada do usuário
classe_personagem = input("Digite a classe do personagem (guerreiro, mago ou arqueiro): ").lower()
pontos_forca = int(input("Digite os pontos de Força do personagem: "))
pontos_magia = int(input("Digite os pontos de Magia do personagem: "))

# Validar a ficha do personagem
resultado = validar_ficha_personagem(classe_personagem, pontos_forca, pontos_magia)

# Imprimir o resultado
print(resultado)