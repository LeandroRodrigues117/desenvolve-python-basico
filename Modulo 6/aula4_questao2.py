frase = input("Digite uma frase: ").lower()


vogais = 'aeiou'


lista_vogais = sorted([letra for letra in frase if letra in vogais and letra.isalpha()])


lista_consoantes = [letra for letra in frase if letra.isalpha() and letra not in vogais]


print("Lista de vogais (ordenada alfabeticamente):", lista_vogais)
print("Lista de consoantes:", lista_consoantes)