import json
import os
from time import sleep

usuarios = {}

itens_menu = {
    "hamburgueres": {
        "1": {"nome": "Clássico", "ingredientes": "Pão Brioche, Hambúrguer Bovino 180g, Queijo Cheddar, Alface, Tomate, Cebola, Molho Mostarda", "kcal": 700, "valor": 34.90},
        "2": {"nome": "Porco com Queijo", "ingredientes": "Pão Brioche, Carne de Porco 180g, Queijo Gruyère, Bacon, Picles", "kcal": 800, "valor": 39.00},
        "3": {"nome": "Bacon Mania", "ingredientes": "Pão Australiano, Hambúrguer Angus 180g, Queijo Mussarela, Bacon, Alface, Tomate, Molho Barbecue", "kcal": 750, "valor": 23.90},
        "4": {"nome": "Explosão de Sabor", "ingredientes": "Pão Australiano, Hambúrguer Angus 180g, Queijo Cheddar, Bacon, Alface, Tomate, Molho Maionese", "kcal": 780, "valor": 30.00},
        "5": {"nome": "Frango Grelhado", "ingredientes": "Pão Integral, Peito de Frango Grelhado 180g, Queijo Prato, Presunto, Alface, Tomate, Molho Ketchup", "kcal": 600, "valor": 29.90}
    },
    "acompanhamentos": {
        "1": {"nome": "Batata Rústica", "porção": "100g", "kcal": 200, "valor": 20.00},
        "2": {"nome": "Batata Canoa", "porção": "100g", "kcal": 220, "valor": 20.00},
        "3": {"nome": "Batata Frita", "porção": "100g", "kcal": 300, "valor": 15.00},
        "4": {"nome": "Batata Bacon", "porção": "100g", "kcal": 350, "valor": 25.00},
        "5": {"nome": "Onion Rings", "porção": "100g", "kcal": 250, "valor": 20.00}
    },
    "bebidas": {
        "1": {"nome": "Água com gás", "kcal": 0, "valor": 5.00},
        "2": {"nome": "Água sem gás", "kcal": 0, "valor": 4.00},
        "3": {"nome": "Suco de Laranja", "kcal": 120, "valor": 8.00},
        "4": {"nome": "Suco de Acerola", "kcal": 100, "valor": 8.00},
        "5": {"nome": "Suco de Caja", "kcal": 110, "valor": 8.50},
        "6": {"nome": "Guaraná Antarctica", "kcal": 150, "valor": 10.00},
        "7": {"nome": "Coca-Cola", "kcal": 140, "valor": 10.00},
        "8": {"nome": "Fanta", "kcal": 160, "valor": 10.00}
    }
}

numero_pedido = 0
contador_pedidos = 0
pedido = {}

def cadastrar_usuario(cpf, nome, numero_telefone, genero, idade, observacoes):
    if cpf not in usuarios:
        usuarios[cpf] = {
            "CPF": cpf,
            "Nome": nome,
            "Numero": numero_telefone,
            "Gênero": genero,
            "Idade": idade,
            "Observações": observacoes
        }
        print("Usuário cadastrado com sucesso!")
    else:
        print("CPF já cadastrado!")

def login(cpf):
    if cpf in usuarios:
        print("Login bem sucedido! Bem-vindo,", usuarios[cpf]["Nome"])
    else:
        print("CPF não encontrado!")

def entrar_como_visitante():
    print("Início de atendimento!")

class Cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'

arquivo = os.path.join(os.path.dirname(__file__), 'codigo_produto.json')

def verificar_arquivo_produto():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f)

def cadastrar_produto(codigo_produto, tipo_produto):
    with open(arquivo, 'r') as f:
        codigo_produtos = json.load(f)
        
    codigo_produtos.append({"codigo": codigo_produto, "tipo": tipo_produto})

    with open(arquivo, 'w') as f:
        json.dump(codigo_produtos, f, indent=4)
    print("Produto cadastrado com sucesso!")
    
def listar_produtos():
    with open(arquivo, 'r') as f:
        codigo_produtos = json.load(f)

    if codigo_produtos:
        print("=" * 50)
        print("LISTA DE PRODUTOS:")
        print("-" * 50)
        for produto in codigo_produtos:
            print("*" * 50)
            print(f"TIPO: {produto['tipo']}, CODIGO: {produto['codigo']}")
            print("*" * 50)
            print("=" * 50)
    else:
        print("NENHUM PRODUTO CADASTRADO.")

def atualizar_produto(codigo_produto_antigo, novo_codigo_produto, novo_tipo_produto):
    with open(arquivo, 'r') as f:
        codigo_produtos = json.load(f)

    for produto in codigo_produtos:
        if produto['codigo'] == codigo_produto_antigo:
            produto['codigo'] = novo_codigo_produto
            produto['tipo'] = novo_tipo_produto
            break

    with open(arquivo, 'w') as f:
        json.dump(codigo_produtos, f, indent=4)
    print("PRODUTO ATUALIZADO COM SUCESSO!")

def excluir_produto(codigo_produto):
    with open(arquivo, 'r') as f:
        codigo_produtos = json.load(f)

    codigo_produtos = [produto for produto in codigo_produtos if produto['codigo'] != codigo_produto]

    with open(arquivo, 'w') as f:
        json.dump(codigo_produtos, f, indent=4)
    print("PRODUTO EXCLUÍDO COM SUCESSO!")

def buscar_produto(codigo_produto):
    with open(arquivo, 'r') as f:
        codigo_produtos = json.load(f)
    
    encontrado = False

    for produto in codigo_produtos:
        if produto['codigo'] == codigo_produto:
            print(f"CODIGO: {produto['codigo']}, TIPO: {produto['tipo']}")
            encontrado = True
            break
    if not encontrado:
        print("NENHUM PRODUTO CADASTRADO COM ESSE CÓDIGO.")

def mostrar_menu(categoria):
    print(f"Menu de {categoria}:")
    for numero, item in itens_menu[categoria].items():
        if categoria == "bebidas":
            print(f"{numero}: {item['nome']} - {item['kcal']} kcal - Valor: R${item['valor']:.2f}")
        elif categoria == "hamburgueres":
            print(f"{numero}: {item['nome']} - Ingredientes: {item['ingredientes']} - {item['kcal']} kcal - Valor: R${item['valor']:.2f}")
        elif categoria == "acompanhamentos":
            print(f"{numero}: {item['nome']} - Porção: {item['porção']} - {item['kcal']} kcal - Valor: R${item['valor']:.2f}")

def fazer_pedido():
    global contador_pedidos, pedido, numero_pedido
    contador_pedidos += 1
    numero_pedido = contador_pedidos
    print(f"Pedido nº {numero_pedido}\n")
    
    pedido = {}
    
    for categoria in itens_menu:
        mostrar_menu(categoria)
        while True:
            escolha = input(f"Escolha um item de {categoria} ou digite 's' para sair: ")
            if escolha == 's':
                break
            if escolha in itens_menu[categoria]:
                quantidade = int(input("Digite a quantidade: "))
                item = itens_menu[categoria][escolha]
                if item['nome'] in pedido:
                    pedido[item['nome']]['quantidade'] += quantidade
                else:
                    pedido[item['nome']] = {'quantidade': quantidade, 'kcal': item['kcal'], 'valor': item['valor']}
            else:
                print("Escolha inválida, tente novamente.")

    mostrar_resumo(numero_pedido)
    editar_pedido(numero_pedido)
    adicionar_comentario()

def mostrar_resumo(numero_pedido):
    print(f"\nResumo do pedido nº {numero_pedido}:")
    total_kcal = 0
    total_valor = 0
    for i, (item, detalhes) in enumerate(pedido.items(), 1):
        total_kcal += detalhes['kcal'] * detalhes['quantidade']
        total_valor += detalhes['valor'] * detalhes['quantidade']
        print(f"{i}. {detalhes['quantidade']}x {item} - {detalhes['kcal']} kcal - Valor: R${detalhes['valor'] * detalhes['quantidade']:.2f}")
    print(f"Total de kcal do pedido: {total_kcal} kcal")
    print(f"Valor total do pedido: R${total_valor:.2f}")

def editar_pedido(numero_pedido):
    while True:
        resposta = input("Deseja alterar algum item do pedido? (S/N): ")
        if resposta.upper() == 'S':
            item_para_alterar = input("Digite o número do item que deseja alterar ou 'A' para adicionar mais itens: ")
            if item_para_alterar.upper() == 'A':
                for categoria in itens_menu:
                    mostrar_menu(categoria)
                    while True:
                        escolha = input(f"Escolha um item de {categoria} ou digite 's' para sair: ")
                        if escolha == 's':
                            break
                        if escolha in itens_menu[categoria]:
                            quantidade = int(input("Digite a quantidade: "))
                            item = itens_menu[categoria][escolha]
                            if item['nome'] in pedido:
                                pedido[item['nome']]['quantidade'] += quantidade
                            else:
                                pedido[item['nome']] = {'quantidade': quantidade, 'kcal': item['kcal'], 'valor': item['valor']}
                        else:
                            print("Escolha inválida, tente novamente.")
                mostrar_resumo(numero_pedido)
            else:
                try:
                    item_para_alterar = int(item_para_alterar) - 1
                    item_nome = list(pedido.keys())[item_para_alterar]
                    nova_quantidade = int(input("Digite a nova quantidade: "))
                    if nova_quantidade == 0:
                        del pedido[item_nome]
                    else:
                        pedido[item_nome]['quantidade'] = nova_quantidade
                    mostrar_resumo(numero_pedido)
                except (ValueError, IndexError):
                    print("Item não encontrado no pedido.")
        elif resposta.upper() == 'N':
            break
        else:
            print("Resposta inválida, por favor digite S ou N.")

def adicionar_comentario():
    comentario = input("Deseja adicionar um comentário ao pedido? (Deixe em branco para nenhum): ")
    if comentario:
        print(f"Comentário adicionado: {comentario}")
    else:
        print("Nenhum comentário adicionado.")
    print("Obrigado por fazer seu pedido!")

def menu_inicial():
    print(Cor.AZUL + "=" * 65 + Cor.RESET)
    print(Cor.VERMELHO + "  ---------->>>>>CADASTRO DE PRODUTOS E USUÁRIOS<<<<<----------")
    print("          1 -- MENU DE CADASTROS DE USUÁRIOS")
    print("          2 -- MENU DE CADASTROS DE PRODUTOS")
    print("          3 -- FAZER PEDIDO")
    print("          4 -- SAIR")
    print(Cor.AZUL + "=" * 65 + Cor.RESET)

def menu_usuarios():
    print("\nMENU DE USUÁRIOS!")
    print("1. CADASTRAR USUÁRIO")
    print("2. LOGIN")
    print("3. ENTRAR COMO VISITANTE")
    print("4. VOLTAR AO MENU ANTERIOR")
    print("5. SAIR")

def menu_produtos():
    print("\nMENU DE PRODUTOS!")
    print("1. CADASTRAR PRODUTO")
    print("2. LISTAR PRODUTOS")
    print("3. BUSCAR PRODUTO")
    print("4. EDITAR PRODUTO")
    print("5. EXCLUIR PRODUTO")
    print("6. VOLTAR AO MENU ANTERIOR")
    print("7. SAIR")

def main():
    verificar_arquivo()

    while True:
        menu_inicial()
        escolha = input("ESCOLHA UMA OPÇÃO:\n>>> ")

        if escolha == "1":
            while True:
                menu_usuarios()
                opcao = input("ESCOLHA UMA OPÇÃO:\n>>> ")

                if opcao == "1":
                    cpf = input("Digite seu CPF: ")
                    nome = input("Digite seu Nome: ")
                    numero_telefone = input("Digite seu número de telefone: ")
                    genero = input("Digite seu gênero: ")
                    idade = int(input("Digite sua idade: "))
                    observacoes = input("Se você tiver coisas que não pode comer: ")
                    cadastrar_usuario(cpf, nome, numero_telefone, genero, idade, observacoes)

                elif opcao == "2":
                    cpf = input("Digite seu CPF: ")
                    login(cpf)
                    break

                elif opcao == "3":
                    entrar_como_visitante()
                    print("Você entrou como visitante!")
                    break

                elif opcao == "4":
                    print("VOLTAR AO MENU ANTERIOR...")
                    sleep(3)
                    break

                elif opcao == "5":
                    print("Saindo...")
                    break

                else:
                    print("Opção inválida!")

        elif escolha == "2":
            while True:
                menu_produtos()
                opcao = input("ESCOLHA UMA OPÇÃO:\n>>> ")

                if opcao == "1":
                    codigo_produto = input("CODIGO DO PRODUTO:\n>>> ")
                    tipo_produto = input("TIPO DO PRODUTO:\n>>> ")
                    cadastrar_produto(codigo_produto, tipo_produto)
                    
                elif opcao == "2":
                    listar_produtos()

                elif opcao == "3":
                    codigo_produto = input("CODIGO DO PRODUTO: ")
                    buscar_produto(codigo_produto)

                elif opcao == "4":
                    codigo_produto_antigo = input("DIGITE O CODIGO A SER MUDADO:\n>>> ")
                    novo_codigo_produto = input("DIGITE O NOVO CODIGO DO PRODUTO:\n>>> ")
                    novo_tipo_produto = input("DIGITE O TIPO DO PRODUTO:\n>>> ")
                    atualizar_produto(codigo_produto_antigo, novo_codigo_produto, novo_tipo_produto)

                elif opcao == "5":
                    codigo_produto = input("DIGITE O CODIGO PARA SER EXCLUÍDO:\n>>> ")
                    excluir_produto(codigo_produto)

                elif opcao == "6":
                    print("VOLTAR AO MENU ANTERIOR...")
                    sleep(3)
                    break

                elif opcao == "7":
                    print("🚀 SAINDO...")
                    sleep(3)
                    break

                else:
                    print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

        elif escolha == "3":
            fazer_pedido()

        elif escolha == "4":
            print("🚀 SAINDO...")
            sleep(3)
            break

        else:
            print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()
