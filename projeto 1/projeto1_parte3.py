def cadastrar_produto():
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preço do produto: "))
    
    return {"codigo": codigo, "nome": nome, "quantidade": quantidade, "preco": preco}

def info_produto(produto):
    print("\nInformações do Produto:")
    print(f"Código: {produto['codigo']}")
    print(f"Nome: {produto['nome']}")
    print(f"Quantidade: {produto['quantidade']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    
    valor_total = produto['quantidade'] * produto['preco']
    print(f"Valor total da compra: R$ {valor_total:.2f}")

produto = cadastrar_produto()

info_produto(produto)