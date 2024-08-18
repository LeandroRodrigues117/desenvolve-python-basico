import random


num_elementos = random.randint(5, 20)


elementos = [random.randint(1, 10) for _ in range(num_elementos)]


print("Lista elementos:")
print(elementos)

soma_elementos = sum(elementos)
print("\nSoma dos valores da lista elementos:", soma_elementos)

media_elementos = soma_elementos / num_elementos
print("Média dos valores da lista elementos:", media_elementos)
