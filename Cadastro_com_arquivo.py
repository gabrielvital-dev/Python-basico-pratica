usuarios = []

def cadastrar_usuario():
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    usuarios.append({"nome": nome, "email": email})
    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    for i, usuario in enumerate(usuarios):
        print(f"{i} - {usuario['nome']} ({usuario['email']})")

def atualizar_usuario():
    listar_usuarios()
    indice = int(input("Digite o índice do usuário a atualizar: "))
    usuarios[indice]["nome"] = input("Novo nome: ")
    usuarios[indice]["email"] = input("Novo email: ")
    print("Usuário atualizado com sucesso!")

def excluir_usuario():
    listar_usuarios()
    indice = int(input("Digite o índice do usuário a excluir: "))
    usuarios.pop(indice)
    print("Usuário excluído com sucesso!")

while True:
    print("\n1 - Cadastrar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Excluir")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        atualizar_usuario()
    elif opcao == "4":
        excluir_usuario()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")
