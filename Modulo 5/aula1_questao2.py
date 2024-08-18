import random
import math

n = int(input("Digite a quantidade de valores: "))
soma = 0
for i in range(n):
    soma = soma + random.randint(0, 100)

print(f"A raiz quadrada dessa soma é: , {math.sqrt(soma):.2f}")


