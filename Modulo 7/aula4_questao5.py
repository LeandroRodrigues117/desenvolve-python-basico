import csv


livros = [
    {"Título": "1984", "Autor": "George Orwell", "Ano de publicação": 1949, "Número de páginas": 328},
    {"Título": "Brave New World", "Autor": "Aldous Huxley", "Ano de publicação": 1932, "Número de páginas": 311},
    {"Título": "To Kill a Mockingbird", "Autor": "Harper Lee", "Ano de publicação": 1960, "Número de páginas": 281},
    {"Título": "The Great Gatsby", "Autor": "F. Scott Fitzgerald", "Ano de publicação": 1925, "Número de páginas": 180},
    {"Título": "Moby Dick", "Autor": "Herman Melville", "Ano de publicação": 1851, "Número de páginas": 635},
    {"Título": "Pride and Prejudice", "Autor": "Jane Austen", "Ano de publicação": 1813, "Número de páginas": 279},
    {"Título": "The Catcher in the Rye", "Autor": "J.D. Salinger", "Ano de publicação": 1951, "Número de páginas": 277},
    {"Título": "The Hobbit", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1937, "Número de páginas": 310},
    {"Título": "Fahrenheit 451", "Autor": "Ray Bradbury", "Ano de publicação": 1953, "Número de páginas": 158},
    {"Título": "Jane Eyre", "Autor": "Charlotte Brontë", "Ano de publicação": 1847, "Número de páginas": 500},
]


nome_arquivo = "meus_livros.csv"


with open(nome_arquivo, mode="w", newline='', encoding="utf-8") as arquivo_csv:
   
    writer = csv.DictWriter(arquivo_csv, fieldnames=["Título", "Autor", "Ano de publicação", "Número de páginas"])
    
    writer.writeheader()
    
   
    writer.writerows(livros)

print(f"Arquivo '{nome_arquivo}' criado com sucesso.")