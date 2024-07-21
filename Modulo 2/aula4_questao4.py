valor = int(input("Digite o valor: "))

notas_100 = valor // 100
valor = valor % 100

notas_50 = valor // 50
valor = valor % 50

notas_20 = valor // 20
valor = valor % 20

notas_10 = valor // 10
valor = valor % 10

notas_5 = valor // 5
valor = valor % 5

notas_2 = valor // 2
valor = valor % 2

notas_1 = valor 

print (f"{notas_100} nota(s) de 100")
print (f"{notas_50} nota(s) de 50")
print (f"{notas_20} nota(s) de 20")
print (f"{notas_10} nota(s) de 10")
print (f"{notas_5} nota(s) de 5")
print (f"{notas_2} nota(s) de 2")
print (f"{notas_1} nota(s) de 1")