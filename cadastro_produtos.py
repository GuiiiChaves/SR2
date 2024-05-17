import json
import os
from time import sleep

class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'

arquivo = os.path.join(os.path.dirname(__file__), 'codigo_produto.json')

def cadastrar_produto(codigo_produto, tipo_produto):
    with open(arquivo, 'r') as f:
        codigo_produtos = json.load(f)
        
    codigo_produtos.append({"codigo": codigo_produto, "tipo":tipo_produto})

    with open(arquivo, 'w') as f:
        json.dump(arquivo, f, indent=4)
    print(" Produto cadastrado com sucesso!")
    
def listar_produtos():
    with open(arquivo, 'r') as f:
        codigo_produtos = json.load(f)

    if codigo_produtos:
        print("=" *50)
        print("LISTA DE PRODUTOS:")
        print("-" *50)
        for codigos_produtos in codigo_produtos:
            print("*" *50)
            print(f"TIPO: {codigos_produtos['tipo']}, CODIGO: {codigos_produtos['codigo']}")
            print("*" *50)
            print("=" *50)
    else:
        print("NENHUM USUÁRIO CADASTRADO.")

def atualizar_produto(codigo_produto_antigo, novo_codigo_produto, novo_tipo_produto):
    with open(arquivo, 'r') as f:
        codigo_produtos = json.load(f)

    for codigos_produtos in codigo_produtos:
        if codigos_produtos['codigo'] == codigo_produto_antigo:
            codigos_produtos['codigo'] = novo_codigo_produto
            codigos_produtos['tipo'] = novo_tipo_produto
            break

    with open(arquivo, 'w') as f:
        json.dump(codigo_produtos, f, indent=4)
    print("PRODUTO ATUALIZADO COM SUCESSO!")

def excluir_produto(codigo_produto):
    with open(arquivo, 'r') as f:
        codigo_produto = json.load(f)

    for codigos_produtos in codigo_produtos:  
        if codigos_produtos['codigo'] == codigo_produto:
            codigo_produtos.remove(codigos_produtos)

    with open(arquivo, 'w') as f:
        json.dump(codigo_produto, f, indent=4)
        print("PRODUTO EXCLUÍDO COM SUCESSO!")

def buscar_produto(codigo_produto):
    with open(arquivo, 'r') as f:
        codigo_produtos = json.load(f)
    
    encontrado = False

    for codigos_produtos in codigo_produtos:
        if codigos_produtos['nome'] == codigo_produto:
            print(f"CODIGO: {codigos_produtos['codigo']}, TIPO: {codigos_produtos['tipo']}")
            encontrado = True
    if not encontrado:
            print("NENHUM PRODUTO CADASTRADO.")

def linha_horizontal(cor):
    return cor + "=" * 50 + cor['RESET']

def menu_inicial():
    print (cor.AZUL + "=" *55 + cor.RESET)
    print (cor.VERMELHO + "  ---------->>>>>CADASTRO DE PRODUTOS<<<<<----------")
    print("          1 -- MENU DE CADASTROS")
    print("          2 -- SAIR")
    print (cor.AZUL + "=" *55 + cor.RESET)

def menu_produtos():
    print("\nMENU DE CADASTROS!")
    print("1. CADASTRAR PRODUTO")
    print("2. LISTAR PRODUTOS")
    print("3. BUSCAR PRODUTO JA CADASTRADO")
    print("4. EDITAR PRODUTO")
    print("5. EXCLUIR PRODUTO")
    print("6. SAIR")

def main():

    while True:
        menu_inicial()
        escolha = int(input("Escolha uma das opcoes: "))

        match (escolha):

            case 1:
                while True:
                    menu_produtos()
                    opcao = input("ESCOLHA UMA OPÇÃO:\n>>>")

                    if opcao == "1":
                        codigo_produto = input("CODIGO DO PRODUTO:\n>>> ")
                        tipo_produto = input("TIPO DO PRODUTO:\n>>> ")
                        cadastrar_produto(codigo_produto, tipo_produto)
                        
                    elif opcao == "2":
                        listar_produtos()

                    elif opcao == "3":
                        codigo_produto_antigo = input("DIGITE O CODIGO A SER MUDADO:\n>>> ")
                        novo_codigo_produto = input("DIGITE O NOVO CODIGO DO PRODUTO:\n>>> ")
                        novo_tipo_produto = input("DIGITE SE O TIPO MUDOU:\n>>> ")
                        atualizar_produto(codigo_produto_antigo, novo_codigo_produto, novo_tipo_produto)

                    elif opcao == "4":
                        codigo_produto = input("CODIGO DO PRODUTO: ")
                        buscar_produto(codigo_produto)

                    elif opcao == "5":
                        codigo_produto = input("DIGITE O CODIGO PARA SER EXCLUIDO:\n>>> ")
                        excluir_produto(codigo_produto)

                    elif opcao == "6":
                        print("🚀 SAINDO...")
                        sleep(3)
                        break

                    else:
                        print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

            case 2:
                print("🚀 SAINDO...")
                sleep(3)
                break

            case __:
                print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
    
if __name__ == "__main__":
    main()
    
