import csv

# Arquivo de usuários
USERS_FILE = 'usuarios.csv'

# Arquivo de produtos
PRODUCTS_FILE = 'produtos.csv'

# Função para carregar usuários
def load_users():
    users = []
    with open(USERS_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users

# Função para salvar usuários
def save_users(users):
    with open(USERS_FILE, 'w', newline='') as file:
        fieldnames = ['id', 'nome', 'senha', 'tipo']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)

# Função para adicionar um usuário
def add_user(id, nome, senha, tipo):
    users = load_users()
    users.append({'id': id, 'nome': nome, 'senha': senha, 'tipo': tipo})
    save_users(users)

# Função para listar usuários
def list_users():
    users = load_users()
    for user in users:
        print(user)

# Função para atualizar um usuário
def update_user(id, nome=None, senha=None, tipo=None):
    users = load_users()
    for user in users:
        if user['id'] == id:
            if nome:
                user['nome'] = nome
            if senha:
                user['senha'] = senha
            if tipo:
                user['tipo'] = tipo
            break
    save_users(users)

# Função para deletar um usuário
def delete_user(id):
    users = load_users()
    users = [user for user in users if user['id'] != id]
    save_users(users)

# Função para carregar produtos
def load_products():
    products = []
    with open(PRODUCTS_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)
    return products

# Função para salvar produtos
def save_products(products):
    with open(PRODUCTS_FILE, 'w', newline='') as file:
        fieldnames = ['codigo', 'nome', 'preco', 'quantidade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

# Função para adicionar um produto
def add_product(codigo, nome, preco, quantidade):
    products = load_products()
    products.append({'codigo': codigo, 'nome': nome, 'preco': preco, 'quantidade': quantidade})
    save_products(products)

# Função para listar produtos
def list_products():
    products = load_products()
    for product in products:
        print(product)

# Função para atualizar um produto
def update_product(codigo, nome=None, preco=None, quantidade=None):
    products = load_products()
    for product in products:
        if product['codigo'] == codigo:
            if nome:
                product['nome'] = nome
            if preco:
                product['preco'] = preco
            if quantidade:
                product['quantidade'] = quantidade
            break
    save_products(products)

# Função para deletar um produto
def delete_product(codigo):
    products = load_products()
    products = [product for product in products if product['codigo'] != codigo]
    save_products(products)

# Função para buscar produto por nome
def search_product_by_name(name):
    products = load_products()
    result = [product for product in products if name.lower() in product['nome'].lower()]
    return result

# Função para imprimir produtos ordenados por nome
def print_products_sorted_by_name():
    products = load_products()
    products_sorted = sorted(products, key=lambda x: x['nome'])
    for product in products_sorted:
        print(product)

# Função para imprimir produtos ordenados por preço
def print_products_sorted_by_price():
    products = load_products()
    products_sorted = sorted(products, key=lambda x: float(x['preco']))
    for product in products_sorted:
        print(product)

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo de criação de usuários
    add_user('1', 'admin', 'senha123', 'Administrador')
    add_user('2', 'funcionario1', 'senha456', 'Funcionário')
    
    # Exemplo de criação de produtos
    add_product('001', 'Laptop', '3000', '10')
    add_product('002', 'Smartphone', '1500', '20')

    # Listar usuários e produtos
    print("Usuários:")
    list_users()
    print("Produtos:")
    list_products()
    
    # Atualizar e deletar produtos
    update_product('001', preco='2800')
    delete_product('002')

    print("Produtos após atualização e exclusão:")
    list_products()

    # Buscar e ordenar produtos
    print("Busca por nome 'Laptop':")
    print(search_product_by_name('Laptop'))
    
    print("Produtos ordenados por nome:")
    print_products_sorted_by_name()

    print("Produtos ordenados por preço:")
    print_products_sorted_by_price()