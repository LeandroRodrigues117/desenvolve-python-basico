#Leitura de dados (entrada)

nome_produto1 = (input("Digite o nome do produto: "))
preço_produto1 = float(input("Digite o preço do produto: "))
quantidade_produto1 = int(input("Digite a quantidade do produto: "))

nome_produto2 = (input("Digite o nome do produto 2: "))
preço_produto2 = float(input("Digite o preço do produto 2: "))
quantidade_produto2 = int(input("Digite a quantidade do produto 2: "))

nome_produto3 = (input("Digite o nome do produto 3: "))
preço_produto3 = float(input("Digite o preço do produto 3: "))
quantidade_produto3 = int(input("Digite a quantidade do produto 3: "))

#Processamento 
valor_total = (quantidade_produto1 * preço_produto1) + (quantidade_produto2 * preço_produto2) + (quantidade_produto3 * preço_produto3)

#Impressão de dados 
print (f"O preço total da compra é: {valor_total:,.2f}")

