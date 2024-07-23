idade_usuario = int(input("Qual a idade do usuario? "))
numero_jogos =  int(input("Jogou quantos jogos de tabuleiro? "))
print (numero_jogos >= 3 )
vitorias_jogos = int(input("Quantas vezes venceu um jogo? "))

apto_clube = idade_usuario == 17 and numero_jogos >= 3 and vitorias_jogos >=1
print (apto_clube)