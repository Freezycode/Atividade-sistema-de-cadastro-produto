produtos = []

def cadastro_produto(codigo, nome, preco, quantidade):
    produto = {"codigo": codigo, "nome": nome, "preco": preco, "quantidade": quantidade}
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("Lista de Produtos:")
        for i, produto in enumerate(produtos):
            print(f"{i + 1} - Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R$ {produto['preco']:.2f}, Quantidade: {produto['quantidade']}")

def buscar_produto(termo):
    achados = []
    for i, produto in enumerate(produtos):
        if produto['codigo'] == termo or produto['nome'].lower() == termo.lower():
            achados.append((i, produto))
    return achados

def atualizar_produto(indice, nomeNovo, precoNovo, quantidadeNova):
    if 0 <= indice < len(produtos):
        produtos[indice]['nome'] = nomeNovo
        produtos[indice]['preco'] = precoNovo
        produtos[indice]['quantidade'] = quantidadeNova
        print("Produto atualizado com sucesso!")
    else:
        print("Índice inválido.")

def excluir_produto(indice):
    if 0 <= indice < len(produtos):
        produtos.pop(indice)
        print("Produto excluído com sucesso.")
    else:
        print("Índice inválido.")

def valor_total_estoque():
    total = sum(produto['preco'] * produto['quantidade'] for produto in produtos)
    print(f"Valor total do estoque: R$ {total:.2f}")

while True:
    print("Escolha uma das opções:")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Buscar Produto")
    print("4 - Atualizar Produto")
    print("5 - Deletar Produto")
    print("6 - Quantidade total do estoque")
    print("7 - Sair")

    escolha = input("Digite a opção desejada: ")

    if escolha == "1":
        codigo = input("Digite o código do produto: ")
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: ").replace(",", "."))
        quantidade = int(input("Digite a quantidade do produto: "))
        cadastro_produto(codigo, nome, preco, quantidade)

    elif escolha == "2":
        listar_produtos()

    elif escolha == "3":
        termo = input("Digite o código ou nome do produto que deseja buscar: ")
        resultados = buscar_produto(termo)
        if resultados:
            for i, p in resultados:
                print(f"{i + 1} - Código: {p['codigo']}, Nome: {p['nome']}, Preço: R$ {p['preco']:.2f}, Quantidade: {p['quantidade']}")
        else:
            print("Produto não encontrado.")

    elif escolha == "4":
        listar_produtos()
        indice = int(input("Digite o número do produto que deseja atualizar: ")) - 1
        nomeNovo = input("Digite o novo nome do produto: ")
        precoNovo = float(input("Digite o novo preço do produto: ").replace(",", "."))
        quantidadeNova = int(input("Digite a nova quantidade do produto: "))
        atualizar_produto(indice, nomeNovo, precoNovo, quantidadeNova)

    elif escolha == "5":
        listar_produtos()
        indice = int(input("Digite o número do produto que deseja deletar: ")) - 1
        excluir_produto(indice)

    elif escolha == "6":
        valor_total_estoque()

    elif escolha == "7":
        print("Saindo")
        break

    else:
        print("Opção inválida.")
