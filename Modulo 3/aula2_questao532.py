genero = (input("Digite seu genero: "))
idade = int(input("Digite sua idade: "))
tempo_serviço = int(input("Digite seu tempo de serviço: "))

a = (genero == "feminino" and idade >= 60) or (genero == "masculino" and idade >= 65)
b = tempo_serviço > 30
c = idade >= 60 and tempo_serviço >= 25 

pode_aposentar = a or b or c

print (pode_aposentar)