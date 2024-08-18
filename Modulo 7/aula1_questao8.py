def calcular_digito_verificador(digitos, pesos):
    soma = sum(d * p for d, p in zip(digitos, pesos))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def validar_cpf(cpf):
   
    cpf = cpf.replace('.', '').replace('-', '')
    

    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"
    
   
    digitos = list(map(int, cpf[:9]))
    
    pesos_primeiro = list(range(10, 1, -1))
    primeiro_digito = calcular_digito_verificador(digitos, pesos_primeiro)
    
    
    digitos.append(primeiro_digito)
    pesos_segundo = list(range(11, 1, -1))
    segundo_digito = calcular_digito_verificador(digitos, pesos_segundo)
    
    
    return "Válido" if cpf[-2:] == f"{primeiro_digito}{segundo_digito}" else "Inválido"

cpf_input = input("Digite o CPF (no formato XXX.XXX.XXX-XX): ")
resultado = validar_cpf(cpf_input)
print(resultado)