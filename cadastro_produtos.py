import json
import os

class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'

arquivo = os.path.join(os.path.dirname(__file__), 'adimin.json')

def cadastrar_produto(codigo_hamburguer, codigo_bebida, codigo_acompanhamento):
    with open(arquivo, "r") as f:
        codigo_hamburguer = json.load(f)
        codigo_acompanhamento = json.load(f)
        codigo_bebida = json.load(f)
        
        
    codigo_hamburguer.append({"codigo": codigo_hamburguer})
    codigo_bebida.append({"codigo": codigo_bebida})
    codigo_acompanhamento.append({"codigo": codigo_acompanhamento})
    
    with open(arquivo, "w") as f:
        json.dump(arquivo, f, indent=4)
    print(" Produto cadastrado com sucesso!")
    
def listar_produtos():
    with open(arquivo, 'r') as f:
        codigos_produtos = json.load(f)

    if codigos_produtos:
        print("=" *50)
        print("LISTA DE PRODUTOS:")
        print("-" *50)
        for usuario in codigos_produtos:
            print("*" *50)
            print(f"NOME: {usuario['nome']}, IDADE: {usuario['idade']}")
            print("*" *50)
            print("=" *50)
    else:
        print("😒 NENHUM USUÁRIO CADASTRADO.")

def nome_sistema():
    print("---------->>>>>CADASTRO DE PRODUTOS<<<<<----------")

def menu_produtos():
    print("\nMENU DE CADASTROS!")
    print("1 - Hamburguer")
    print("2 - Bebida")
    print("3 - Acompanhamento")
    print("4 - Listar produtos")
    print("4 - Buscar produto já cadastrado")
    print("5 - Ediçäo dos produtos cadastrados")
    print("6 - Excluir produto")

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
    
