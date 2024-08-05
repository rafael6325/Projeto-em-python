def cadastrar_info():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    telefone = input("Digite seu telefone: ")
    email = input("Digite seu e-mail: ")
    
    return {"nome": nome, "idade": idade, "telefone": telefone, "email": email}

def exibir_info(info):
    print("\nInformações Cadastradas:")
    print(f"Nome: {info['nome']}")
    print(f"Idade: {info['idade']} anos")
    print(f"Telefone: {info['telefone']}")
    print(f"E-mail: {info['email']}")

informacoes = cadastrar_info()

exibir_info(informacoes)