num_respondentes = int(input())

soma = 0
cont = 0 

while cont < num_respondentes:
    idade = int(input())
    soma += idade 

    cont += 1 

print (soma)
print (f"A média das idades é {soma/num_respondentes:.0f}anos")