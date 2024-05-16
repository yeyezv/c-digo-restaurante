import os

restaurantes = [{"nome": "Cantina toscana", "categoria": "Italiana", "ativo": True},
                {"nome": "Sushi da Praça", "categoria": "Japonesa", "ativo": False},
                {"nome": "Churrascaria Gaúcha", "categoria": "Brasileira", "ativo": True},
                {"nome": "Padaria Pão Doce", "categoria": "Padaria", "ativo": True}]

def exibir_nome_do_programa():
    print("""
    █▀▀ ▄▀█ █▀▄ ▄▀█ █▀ ▀█▀ █▀█ █▀█ █▀   █▀▄ █▀▀   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀ █▀   █▀█ █▄░█ █░░ █ █▄░█ █▀▀
    █▄▄ █▀█ █▄▀ █▀█ ▄█ ░█░ █▀▄ █▄█ ▄█   █▄▀ ██▄   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄ ▄█   █▄█ █░▀█ █▄▄ █ █░▀█ ██▄""")
    print("")

def menu():
    print('\n1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')

def finalizar_app():
    print("\nFinalizando ...")

def opcao_invalida():
    print("\nDesculpe! Não temos essa opção em nosso sistema.\n")
    input("Digite enter para voltar ao menu principal")
    main()

def voltar_ao_menu():
    input("\nAperte qualquer tecla para voltar ao menu principal")
    main()

def cadastrar_restaurante():
    print("\n\nCadastre-se: ")
    nome_restaurante = input("Qual o nome do seu restaurante?: ")
    categoria_restaurante = input("Qual a categoria do seu restaurante: ")
    ativar_restaurante = input("Você deseja ativar o seu restaurante? (S/N): ")
    restaurante = {"nome": nome_restaurante, "categoria": categoria_restaurante, "ativo": ativar_restaurante.lower() == 's'}
    restaurantes.append(restaurante)

    print(f"\nO {nome_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu()

def listar_restaurantes():
    print(f"\nAqui está a lista de restaurantes cadastrados em nosso sistema: ")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo_ou_nao = "Ativo" if restaurante["ativo"] else "Inativo"
        print(f"Nome: {nome_restaurante}\nCategoria: {categoria_restaurante}\nStatus: {ativo_ou_nao}\n")
        voltar_ao_menu()

def alterar_estado_restaurante():
    print("Olá usuário, vamos alterar o estado do seu restaurante")
    alterar_restaurante = input("Digite o nome do restaurante que você deseja alterar o estado: ")
    restaurante_encontrado = False 
    for restaurante in restaurantes:
        if alterar_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f'O restaurante {alterar_restaurante} foi ATIVADO com sucesso!' if restaurante['ativo'] else f'O restaurante {alterar_restaurante} foi DESATIVADO com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante digitado não foi encontrado em nosso sistema!")
        voltar_ao_menu()

def escolher_opcao():
    try:
        opcao = int(input("\nEscolha uma opção: "))

        if opcao == 1:
            cadastrar_restaurante()
        elif opcao == 2:
            listar_restaurantes()
        elif opcao == 3:
            alterar_estado_restaurante()
        elif opcao == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except ValueError:
        opcao_invalida()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    menu()
    escolher_opcao()

if __name__ == '__main__':
    main()
