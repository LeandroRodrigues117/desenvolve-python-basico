import random

def encrypt(strings):
   
    chave = random.randint(1, 10)
    
    def criptografar_string(s):
        criptografado = []
        for char in s:
            codigo_original = ord(char)
           
            novo_codigo = codigo_original + chave
            
            if novo_codigo > 126:
                novo_codigo = 33 + (novo_codigo - 127)
            criptografado.append(chr(novo_codigo))
        return ''.join(criptografado)
    
    strings_criptografadas = [criptografar_string(s) for s in strings]
    
    return strings_criptografadas, chave

strings = ["hello", "world", "example"]
strings_criptografadas, chave = encrypt(strings)
print(f"Strings criptografadas: {strings_criptografadas}")
print(f"Chave de criptografia: {chave}")