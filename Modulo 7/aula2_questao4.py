import re

def validador_senha(senha):
    
    if len(senha) < 8:
        return False
    
   
    if not re.search(r'[A-Z]', senha):
        return False
    

    if not re.search(r'[a-z]', senha):
        return False
    
    
    if not re.search(r'[0-9]', senha):
        return False
    
   
    if not re.search(r'[@#$%^&+=]', senha):
        return False
    
   
    return True

# Exemplos de uso:
print(validador_senha("Exemplo@123"))  
print(validador_senha("senha"))         
print(validador_senha("Senha1"))        
print(validador_senha("Senha@1"))       