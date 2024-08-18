import re


arquivo_entrada = "frase.txt"
arquivo_saida = "palavras.txt"

def processar_frase(frase):
   
    palavras = re.findall(r'\b\w+\b', frase)
    return palavras


try:
    with open(arquivo_entrada, "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print(f"O arquivo {arquivo_entrada} não foi encontrado.")
    exit()


palavras = processar_frase(conteudo)


with open(arquivo_saida, "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")


with open(arquivo_saida, "r") as arquivo:
    conteudo_saida = arquivo.read()

print("Conteúdo do arquivo 'palavras.txt':")
print(conteudo_saida)