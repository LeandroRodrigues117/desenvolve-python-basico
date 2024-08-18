frase = input("Digite uma frase: ")


vogais = "aeiou"


contador_vogais = 0
indices_vogais = []


for i, char in enumerate(frase):
    if char.lower() in vogais:
        contador_vogais += 1
        indices_vogais.append(i)


print(f"Número total de vogais: {contador_vogais}")


print(f"Índices das vogais: {indices_vogais}")