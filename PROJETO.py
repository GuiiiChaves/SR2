import json
import os
from time import sleep

arquivo = os.path.join(os.path.dirname(__file__), 'codigo_produto.json')
arquivo2 = os.path.join(os.path.dirname(__file__), 'cadastro_clientes.json')
arquivo3 = os.path.join(os.path.dirname(__file__), 'pedidos.json')

numero_pedido = 0
contador_pedidos = 0
pedido = {}

class Cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'

def cadastrar_usuario(cpf, nome, numero_telefone, observacoes):
    with open(arquivo2, 'r') as f:
        usuarios = json.load(f)

    usuarios.append({'CPF': cpf, 'nome': nome, 'número': numero_telefone, 'observacoes': observacoes})

    with open(arquivo2, 'w') as f:
        json.dump(usuarios, f, indent=4)
    print("USUARIO CADASTRADO COM SUCESSO!")

def login(cpf):
    with open(arquivo2, 'r') as f:
        usuarios = json.load(f)
    for usuario in usuarios:
        if usuario['CPF'] == cpf:
            usuarios.read(usuario)

    with open(arquivo2, 'w') as f:
        json.dump(usuarios, f, indent=4)
        print("USUARIO ENCONTRADO COM SUCESSO!")
        

def entrar_como_visitante():
    visitante = input(print("ESCREVA SEU NOME: "))
    print("Início de atendimento!\n OLÁ ", visitante)

def editar_usuario(cpf, nome_novo, numero_novo, observacoes_novas):
    with open(arquivo2, 'r') as f:
        usuarios = json.load(f)

    for usuario in usuarios:
        if usuario['CPF'] == cpf:
            usuario['nome'] = nome_novo
            usuario['número'] = numero_novo
            usuario['observacoes'] = observacoes_novas

    with open(arquivo2, 'w') as f:
        json.dump(usuarios, f, indent=4)
    print("USUÁRIO ATUALIZADO COM SUCESSO!")

def excluir_usuario(cpf):
    with open(arquivo2, 'r') as f:
        usuarios = json.load(f)

    for usuario in usuarios:  
        if usuario['CPF'] == cpf:
            usuarios.remove(usuario)

    with open(arquivo2, 'w') as f:
        json.dump(usuarios, f, indent=4)
        print("USUÁRIO EXCLUÍDO COM SUCESSO!")

def buscar_usuario (cpf):
    with open(arquivo2, 'r') as f:
        usuarios = json.load(f)
    
    encontrado = False

    for usuario in usuarios:
        if usuario['CPF'] == cpf:
            print(f"CPF: {usuario['cpf']}, NOME: {usuario['nome']}, NUMERO: {usuario['numero']}, OBSERVACOES: {usuario['observacoes']}")
            encontrado = True

    if not encontrado:
            print("NENHUM USUÁRIO CADASTRADO.")      

def listar_usuarios():
    with open(arquivo2, 'r') as f:
        usuarios = json.load(f)

    if usuarios:
        print("=" *60)
        print("LISTA DE USUÁRIOS:")
        print("-" *60)
        for usuario in usuarios:
            print("*" *60)
            print(f"CPF: {usuario['cpf']}, NOME: {usuario['nome']}, NUMERO: {usuario['numero']}, OBSERVACOES: {usuario['observacoes']}")
            print("*" *60)
            print("=" *60)      

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
    print("4. EDITAR PERFIL")
    print("5. EXCLUIR PERFIL")
    print("6. LISTAR USUARIOS")
    print("7. VOLTAR AO MENU ANTERIOR")
    print("8. SAIR")

def menu_produtos():
    print("\nMENU DE PRODUTOS!")
    print("1. CADASTRAR PRODUTO")
    print("2. LISTAR PRODUTOS")
    print("3. BUSCAR PRODUTO")
    print("4. EDITAR PRODUTO")
    print("5. EXCLUIR PRODUTO")
    print("6. VOLTAR AO MENU ANTERIOR")
    print("7. SAIR")

def menu_pedidos():
    print("\nESSE É O NOSSO CARDÁPIO!")
    print("1. HAMBURGUERES")
    print("2. BEBIDAS")
    print("3. ACOMPANHAMENTOS")
    print("4. VOLTAR AO MENU ANTERIOR")
    print("5. SAIR")

def menu_hamburguer():
    print("1 -> CLASSICO (780cal) -> INGREDIENTES: pao brioche; hamburguer bovino(180g); queijo cheddar; alface; tomate; cebola; valor --> R$")
    print("2 -> BACON MANIA (830cal) -> INGREDIENTES: pao australiano; hamburguer angus(180g); queijo mussarela; bacon; alface; tomate; cebola; molho barbecue; valor --> R$")
    print("3 -> FRANGO GRELHADO (530cal) -> INGREDIENTES: pao brioche; carne de porco(180g); queijo gruyère; bacon; picles; molho mostarda; valor --> R$")
    print("4 -> PORCO C/ QUEIJO (860cal) -> INGREDIENTES: pao integral; peito de frango grelhado(180g); queijo prato; presunto; tomate; alface; ketchup; valor --> R$")
    print("5 -> EXPLOSAO DE SABOR (855cal) -> INGREDIENTES: pao australiano; hamburguer angus(180g); queijo cheddar; bacon; alface; tomate; maionese; valor --> R$")

def menu_acompanhamento():
    print("1. Batata Rústica; porção: 100g, cal: 200g, valor: 20.00")
    print("2. Batata Canoa; porção: 100g cal: 220, valor: 20.00")
    print("3. Batata Frita; porção: 100g, cal: 300, valor: 15.00")
    print("4. Batata Bacon; porção: 100g, cal: 350, valor: 25.00")
    print("5. Onion Rings; porção: 100g, cal: 250, valor: 20.00")

def menu_bebida():
    print("1. Água com gás, cal: 0, valor: 5.00")
    print("2. Água sem gás, cal: 0, valor: 4.00")
    print("3. Suco de Laranja, cal: 120, valor: 8.00")
    print("4. Suco de Acerola, cal: 100, valor: 8.00")
    print("5. Suco de Caja, cal: 110, valor: 8.50")
    print("6. Guaraná Antarctica, cal: 150, valor: 10.00")
    print("7. Coca-Cola, cal: 140, valor: 10.00")
    print("8. Fanta, cal: 160, valor: 10.00")

def main():
    verificar_arquivo_produto()

    while True:
        menu_inicial()
        escolha = input("ESCOLHA UMA OPÇÃO:\n>>> ")

        match(escolha):
            case 1:
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

            case 2:
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

            case 3:
                while True:
                    menu_pedidos()
                    opcao = input("ESCOLHA UMA OPÇÃO:\n>>> ")

                    if opcao == "1":
                        menu_hamburguer()

                    elif opcao == "2":
                        menu_bebida()

                    elif opcao == "3":
                        menu_acompanhamento()

                    elif opcao == "4":
                        print("VOLTAR AO MENU ANTERIOR...")
                        sleep(3)
                        break
                    
                    elif opcao == "5":
                        print("🚀 SAINDO...")
                        sleep(3)
                        break

                    else:
                        print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

            case 4:
                print("🚀 SAINDO...")
                sleep(3)
                break

            case __:
                print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()
