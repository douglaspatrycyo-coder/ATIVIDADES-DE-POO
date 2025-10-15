# ==========================
# SISTEMA DE ESTOQUE
# ==========================

# 1. Variáveis globais
estoque_comida = {
    "sanduíche": 5,
    "bolo": 4,
    "pizza": 3,
    "hambúrguer": 6,
    "batata frita": 8,
    "salada": 2,
    "sopa": 10,
    "lasanha": 5,
    "pastel": 7,
    "coxinha": 1
}

estoque_bebida = {
    "refrigerante": 10,
    "suco": 8,
    "café": 15,
    "água": 12,
    "cerveja": 6,
    "energético": 4,
    "vitamina": 3,
    "milkshake": 2,
    "chá": 9,
    "vinho": 5
}

# ==========================
# 2. Funções do sistema
# ==========================

def mostrar_estoque():
    """Mostra todos os produtos e suas quantidades."""
    print("\n=== ESTOQUE DE COMIDAS ===")
    for produto, qtd in estoque_comida.items():
        print(f"{produto}: {qtd}")
    print("\n=== ESTOQUE DE BEBIDAS ===")
    for produto, qtd in estoque_bebida.items():
        print(f"{produto}: {qtd}")

def adicionar_produto(nome, quantidade):
    """Adiciona um novo produto ao estoque ou soma à quantidade existente."""
    global estoque_comida, estoque_bebida

    if nome in estoque_comida:
        estoque_comida[nome] += quantidade
    elif nome in estoque_bebida:
        estoque_bebida[nome] += quantidade
    else:
        tipo = input("O produto é (1) comida ou (2) bebida? ")
        if tipo == "1":
            estoque_comida[nome] = quantidade
        elif tipo == "2":
            estoque_bebida[nome] = quantidade
        else:
            print("Tipo inválido! Produto não adicionado.")
            return
    print(f"{quantidade} unidades adicionadas de {nome}.")

def remover_produto(nome, quantidade):
    """Remove certa quantidade do produto (se houver o suficiente)."""
    global estoque_comida, estoque_bebida

    if nome in estoque_comida:
        if estoque_comida[nome] >= quantidade:
            estoque_comida[nome] -= quantidade
            print(f"{quantidade} unidades removidas de {nome}.")
        else:
            print("Quantidade insuficiente no estoque!")
    elif nome in estoque_bebida:
        if estoque_bebida[nome] >= quantidade:
            estoque_bebida[nome] -= quantidade
            print(f"{quantidade} unidades removidas de {nome}.")
        else:
            print("Quantidade insuficiente no estoque!")
    else:
        print("Produto não encontrado!")

def consultar_produto(nome):
    """Mostra a quantidade atual de um produto específico."""
    if nome in estoque_comida:
        print(f"{nome}: {estoque_comida[nome]} unidades (comida)")
    elif nome in estoque_bebida:
        print(f"{nome}: {estoque_bebida[nome]} unidades (bebida)")
    else:
        print("Produto não encontrado!")

def repor_automatico():
    """Aumenta em 5 unidades qualquer item com quantidade menor que 3."""
    for produto in estoque_comida:
        if estoque_comida[produto] < 3:
            estoque_comida[produto] += 5
            print(f"Reposição automática: {produto} agora tem {estoque_comida[produto]} unidades.")
    for produto in estoque_bebida:
        if estoque_bebida[produto] < 3:
            estoque_bebida[produto] += 5
            print(f"Reposição automática: {produto} agora tem {estoque_bebida[produto]} unidades.")

def salvar_relatorio():
    """Gera um arquivo estoque.txt com os produtos e quantidades finais."""
    with open("estoque.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("=== ESTOQUE FINAL DE COMIDAS ===\n")
        for produto, qtd in estoque_comida.items():
            arquivo.write(f"{produto}: {qtd}\n")

        arquivo.write("\n=== ESTOQUE FINAL DE BEBIDAS ===\n")
        for produto, qtd in estoque_bebida.items():
            arquivo.write(f"{produto}: {qtd}\n")
    print("Relatório salvo em 'estoque.txt'.")

# ==========================
# 3. Menu principal
# ==========================

def menu():
    while True:
        print("\n=== MENU DO ESTOQUE ===")
        print("1 - Mostrar estoque")
        print("2 - Adicionar produto")
        print("3 - Remover produto")
        print("4 - Consultar produto")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_estoque()
        elif opcao == "2":
            nome = input("Nome do produto: ").lower()
            quantidade = int(input("Quantidade a adicionar: "))
            adicionar_produto(nome, quantidade)
        elif opcao == "3":
            nome = input("Nome do produto: ").lower()
            quantidade = int(input("Quantidade a remover: "))
            remover_produto(nome, quantidade)
        elif opcao == "4":
            nome = input("Nome do produto: ").lower()
            consultar_produto(nome)
        elif opcao == "5":
            repor_automatico()
            salvar_relatorio()
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# ==========================
# Execução do programa
# ==========================

menu()
