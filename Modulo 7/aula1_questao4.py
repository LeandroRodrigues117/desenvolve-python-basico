numero_celular = input("Digite o número de celular: ")

numero_celular = numero_celular.strip()


if len(numero_celular) == 8:
 
    numero_celular = '9' + numero_celular
elif len(numero_celular) == 9:
    
    if numero_celular[0] != '9':
        print("Número inválido. Um número de celular com 9 dígitos deve começar com 9.")
        exit()


numero_formatado = f"{numero_celular[:2]} {numero_celular[2:7]}-{numero_celular[7:]}"


print(f"Número formatado: {numero_formatado}")