import re


nome_arquivo = "estomago.txt"

def contar_mencoes(texto, nome):
    """Conta o número de menções ao nome no texto."""
    pattern = re.compile(r'\b' + re.escape(nome) + r'\b', re.IGNORECASE)
    return len(pattern.findall(texto))


linhas = []
num_linhas = 0
linha_max_caracteres = ""
conteudo_total = ""


try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            conteudo_total += linha
            linhas.append(linha)
            num_linhas += 1
            if len(linha) > len(linha_max_caracteres):
                linha_max_caracteres = linha
                
except FileNotFoundError:
    print(f"O arquivo {nome_arquivo} não foi encontrado.")
    exit()


print("Primeiras 25 linhas do arquivo:")
for i in range(min(25, len(linhas))):
    print(linhas[i].strip())

print("\nNúmero total de linhas no arquivo:", num_linhas)

print("\nLinha com maior número de caracteres:")
print(linha_max_caracteres.strip())

num_mention_nonato = contar_mencoes(conteudo_total, "Nonato")
num_mention_iria = contar_mencoes(conteudo_total, "Íria")

print("\nNúmero de menções ao nome 'Nonato':", num_mention_nonato)
print("Número de menções ao nome 'Íria':", num_mention_iria)