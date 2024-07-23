def calcular_frete(distancia, peso):
    # Definir as taxas por quilograma baseado na distância
    if distancia <= 100:
        taxa_por_kg = 1.0
    elif distancia <= 300:
        taxa_por_kg = 1.5
    else:
        taxa_por_kg = 2.0
    
    # Calcular o valor do frete baseado no peso e na taxa por quilograma
    valor_frete = peso * taxa_por_kg
    
    # Acrescentar taxa extra para pacotes com peso superior a 10 kg
    if peso > 10:
        valor_frete += 10
    
    return valor_frete

# Exemplo de utilização:
try: 
    distancia = float(input("Digite a distância da entrega em quilômetros: "))
    peso = float(input("Digite o peso do pacote em quilogramas: "))
    
    if distancia <= 0 or peso <= 0:
        raise ValueError("A distância e o peso devem ser maiores que zero.")
    
    frete = calcular_frete(distancia, peso)
    print(f"O valor do frete é R${frete:.2f}")

   
except Exception as e:
    print(f"Erro inesperado: {e}")