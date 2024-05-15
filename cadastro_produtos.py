import os

def nome_sistema():
    print("---------->>>>>CADASTRO DE PRODUTOS<<<<<----------")

def menu_produtos():
    print("SELECIONE QUAL PRODUTO VOCE DESEJA CADASTRAR!")
    print("1 - Hamburguer")
    print("2 - Bebida")
    print("3 - Acompanhamentos")
    print("4 - Buscar um produto")
    print("5 - Edicao de produtos")
    print("6 - Sair")

def volta_menu():
    input("Digite uma tecla para voltar ao menu anterior! ")
    main()

def opcoes():
    escolhas = int(input("Escolha uma das opcoes: "))
    match (escolhas):
        case 1:
            codigo_hamburguer = str(input("Digite o codigo do produto aq: "))
            print("Produto cadastrado com sucesso!", codigo_hamburguer)
            volta_menu()

        case 2:
            codigo_bebida = str(input("Digite o codigo do produto aq: "))
            print("Produto cadastrado com sucesso!", codigo_bebida)
            volta_menu()

        case 3:
            codigo_acompanhamento = str(input("Digite o codigo do produto aq: "))
            print("Produto cadastrado com sucesso!", codigo_acompanhamento)
            volta_menu()

        case 4:
            codigo_busca = str(input("Digite o codigo do produto aqui: "))
            print("Produto encontrado!", codigo_busca)
            volta_menu()

        case 5:
            codigo = str(input("Digite o codigo do produto que voce deseja editar: "))
            print("Proguto escolhido", codigo)
            observacao = str(input("Faca a alteracao: "))
            print(observacao)
            print("Alteracao realizada com sucesso!")
            volta_menu()

        case 6:
            print(" Sistema Finalizado!")

        case __:
            print("Opcao invalida! Digite uma opcao existente!")
            main()
        
def main():
    os.system("cls")
    nome_sistema()
    menu_produtos()
    opcoes()

if __name__ == "__main__":
    main()
    
