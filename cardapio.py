import os
import json

class Cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'

arquivo3 = os.path.join(os.path.dirname(__file__), 'cardapio.json')

def verificar_arquivo_pedidos():
    if not os.path.exists(arquivo3):
        with open(arquivo3, 'w') as file_:
            json.dump([], file_)

def cadastro_pedidos(nome_cliente, numero_pedido, hamburguer, quantidade_hamburguer, bebida, quantidade_bebida, acompanhamento, quantidade_acompanhamento, observacao_pedido):
    with open(arquivo3, 'r') as file_:
        pedidos = json.load(file_)

    pedidos.append({'Nome': nome_cliente, 'Numero do pedido': numero_pedido, 'Hamburguer': hamburguer, 'Quantidade hamburguer': quantidade_hamburguer, 'Bebida': bebida, 'Quantidade bebida': quantidade_bebida, 'Acompanhamento': acompanhamento, 'Quantidade acompanhamento': quantidade_acompanhamento, 'Observacao do pedido': observacao_pedido})

    with open(arquivo3, 'w') as file_:
        json.dump(pedidos, file_, indent=4)
    print("PEDIDO REALIZADO COM SUCESSO!")

def editar_pedido(numero_pedido, novo_hamburguer, nova_quantidade_hamburguer, nova_bebida, nova_quantidade_bebida, novo_acompanhamento, nova_quantidade_acompanhamento, nova_observacao_pedido):
    with open(arquivo3, 'r') as file_:
        pedidos = json.load(file_)

    for pedido in pedidos:
        if pedido['Numero do pedido'] == numero_pedido:
            pedido['Hamburguer'] = novo_hamburguer
            pedido['Quantidade hamburguer'] = nova_quantidade_hamburguer
            pedido['Bebida'] = nova_bebida
            pedido['Quantidade bebida'] = nova_quantidade_bebida
            pedido['Acompanhamento'] = novo_acompanhamento
            pedido['Quantidade acompanhamento'] = nova_quantidade_acompanhamento
            pedido['Observacao do pedido'] = nova_observacao_pedido
            break

    with open(arquivo3, 'w') as file_:
        json.dump(pedidos, file_, indent=4)
    print("PEDIDO ATUALIZADO COM SUCESSO!")

def excluir_pedido(numero_pedido):
    with open(arquivo3, 'r') as file_:
        pedidos = json.load(file_)

    for pedido in pedidos:  
        if pedido['Numero do pedido'] == numero_pedido:
            pedidos.remove(pedido)
            break

    with open(arquivo3, 'w') as file_:
        json.dump(pedidos, file_, indent=4)
    print("PEDIDO EXCLUÍDO COM SUCESSO!")

def listar_pedidos():
    with open(arquivo3, 'r') as file_:
        pedidos = json.load(file_)

    if pedidos:
        print("=" * 215)
        print("LISTA DE PEDIDOS:")
        print("=" * 215)
        for pedido in pedidos:
            print("*" * 215)
            print(f"NOME: {pedido['Nome']}, NUMERO DO PEDIDO: {pedido['Numero do pedido']}, HAMBURGUER: {pedido['Hamburguer']}, QUANTIDADE HAMBURGUER: {pedido['Quantidade hamburguer']}, BEBIDA: {pedido['Bebida']}, QUANTIDADE BEBIDA: {pedido['Quantidade bebida']}, ACOMPANHAMENTO: {pedido['Acompanhamento']}, QUANTIDADE ACOMPANHAMENTO: {pedido['Quantidade acompanhamento']}, OBSERVACAO: {pedido['Observacao do pedido']}")
            print("*" * 215)
        print("=" * 215)
    else:
        print("NENHUM PEDIDO CADASTRADO!.")

def confirmar_pedido():
    confirmacao = input("Deseja confirmar o pedido? (S/N): ").upper()
    return confirmacao == 'S'

def menu_inicial():
    print(Cor.AZUL + "=" * 65 + Cor.RESET)
    print(Cor.VERMELHO + "  ---------->>>>>CADASTRO DE PRODUTOS E USUÁRIOS<<<<<----------")
    print("          1 -- MENU DE CADASTROS DE USUÁRIOS")
    print("          2 -- MENU DE CADASTROS DE PRODUTOS")
    print("          3 -- FAZER PEDIDO")
    print("          4 -- SAIR")
    print(Cor.AZUL + "=" * 65 + Cor.RESET)

def menu_pedidos():
    print("\n========== CARDÁPIO! ==========")
    print("1. HAMBURGUERES")
    print("2. BEBIDAS")
    print("3. ACOMPANHAMENTOS")
    print("4. FINALIZAR PEDIDO")
    print("5. LISTAR PEDIDOS")
    print("6. EDITAR PEDIDO")
    print("7. EXCLUIR PEDIDO")  
    print("8. VOLTAR AO MENU ANTERIOR")

def menu_hamburguer():
    print("1. CLASSICO (780cal) => INGREDIENTES: pao brioche; hamburguer bovino(180g); queijo cheddar; alface; tomate; cebola; valor --> R$25.00")
    print("2. BACON MANIA (830cal) => INGREDIENTES: pao australiano; hamburguer angus(180g); queijo mussarela; bacon; alface; tomate; cebola; molho barbecue; valor --> R$30.00")
    print("3. FRANGO GRELHADO (530cal) => INGREDIENTES: pao brioche; carne de porco(180g); queijo gruyère; bacon; picles; molho mostarda; valor --> R$28.00")
    print("4. PORCO C/ QUEIJO (860cal) => INGREDIENTES: pao integral; peito de frango grelhado(180g); queijo prato; presunto; tomate; alface; ketchup; valor --> R$27.00")
    print("5. EXPLOSAO DE SABOR (855cal) => INGREDIENTES: pao australiano; hamburguer angus(180g); queijo cheddar; bacon; alface; tomate; maionese; valor --> R$32.00")

def menu_acompanhamento():
    print("1. Batata Rústica => porção: 100g, cal: 200g, valor --> R$20.00")
    print("2. Batata Canoa => porção: 100g cal: 220, valor --> R$20.00")
    print("3. Batata Frita => porção: 100g, cal: 300, valor --> R$15.00")
    print("4. Batata c/ Bacon => porção: 100g, cal: 350, valor --> R$25.00")
    print("5. Onion Rings => porção: 100g, cal: 250, valor --> R$20.00")

def menu_bebida():
    print("1. Água com gás => cal: 0, valor --> R$5.00")
    print("2. Água sem gás => cal: 0, valor --> R$4.00")
    print("3. Suco de Laranja => cal: 120, valor --> R$8.00")
    print("4. Suco de Acerola => cal: 100, valor --> R$8.00")
    print("5. Suco de Caja => cal: 110, valor --> R$8.50")
    print("6. Guarana Antartica => cal: 150, valor --> R$10.00")
    print("7. Coca-Cola => cal: 140, valor --> R$10.00")
    print("8. Fanta Laranja => cal: 160, valor --> R$10.00")

def main():
    verificar_arquivo_pedidos()
    
    contador_pedidos = 0
    
    while True:
        menu_inicial()
        escolha = input("ESCOLHA UMA OPÇÃO:\n>>> ")

        if escolha == '1':
            print("CADASTRO DE USUÁRIOS NÃO IMPLEMENTADO!")
            continue
                
        elif escolha == '2':
            print("CADASTRO DE PRODUTOS NÃO IMPLEMENTADO!")
            continue
                
        elif escolha == '3':
            contador_pedidos += 1
            numero_pedido = contador_pedidos
            nome_cliente = input("Informe o seu nome:\n>>> ")
            print(f"Pedido nº {numero_pedido}\n")
                
            hamburguer = None
            quantidade_hamburguer = None
            bebida = None
            quantidade_bebida = None
            acompanhamento = None
            quantidade_acompanhamento = None
            observacao_pedido = None
                
            hamburguer_nome = {
                '1': 'CLASSICO',
                '2': 'BACON MANIA',
                '3': 'FRANGO GRELHADO',
                '4': 'PORCO C/ QUEIJO',
                '5': 'EXPLOSAO DE SABOR'
            }
            bebida_nome = {
                '1': 'AGUA COM GAS',
                '2': 'AGUA SEM GAS',
                '3': 'SUCO DE LARANJA',
                '4': 'SUCO DE ACEROLA',
                '5': 'SUCO DE CAJA',
                '6': 'GUARANA ANTARTICA',
                '7': 'COCA-COLA',
                '8': 'FANTA LARANJA'
            }
            acompanhamento_nome = {
                '1': 'BATATA RUSTICA',
                '2': 'BATATA CANOA',
                '3': 'BATATA FRITA',
                '4': 'BATATA BACON',
                '5': 'Onion Rings'
            }
            
            while True:
                menu_pedidos()
                opcao_pedidos = input("ESCOLHA UMA OPÇÃO:\n>>> ")

                if opcao_pedidos == '1':
                    menu_hamburguer()
                    opcao_hamburguer = input("ESCOLHA UMA OPÇÃO:\n>>> ")
                    hamburguer = hamburguer_nome.get(opcao_hamburguer, "OPCAO INVALIDA")
                    quantidade_hamburguer = int(input("Informe a quantidade desejada:\n>>> "))
                    observacao_pedido = input("Observacao:\n>>> ")
                
                elif opcao_pedidos == '2':
                    menu_bebida()
                    opcao_bebida = input("ESCOLHA UMA OPÇÃO:\n>>> ")
                    bebida = bebida_nome.get(opcao_bebida, "OPCAO INVALIDA")
                    quantidade_bebida = int(input("Informe a quantidade desejada:\n>>> "))
                
                elif opcao_pedidos == '3':
                    menu_acompanhamento()
                    opcao_acompanhamento = input("ESCOLHA UMA OPÇÃO:\n>>> ")
                    acompanhamento = acompanhamento_nome.get(opcao_acompanhamento, "OPCAO INVALIDA")
                    quantidade_acompanhamento = int(input("Informe a quantidade desejada:\n>>> "))
                
                elif opcao_pedidos == '4':
                    print(f"Resumo do pedido nº {numero_pedido}:")
                    print(f"Nome: {nome_cliente}")
                    print(f"Hamburguer: {hamburguer} - Quantidade: {quantidade_hamburguer}")
                    print(f"Bebida: {bebida} - Quantidade: {quantidade_bebida}")
                    print(f"Acompanhamento: {acompanhamento} - Quantidade: {quantidade_acompanhamento}")
                    print(f"Observacao do pedido: {observacao_pedido}")

                    if confirmar_pedido():
                        cadastro_pedidos(nome_cliente, numero_pedido, hamburguer, quantidade_hamburguer, bebida, quantidade_bebida, acompanhamento, quantidade_acompanhamento, observacao_pedido)
                        break

                elif opcao_pedidos == '5':
                    listar_pedidos()

                elif opcao_pedidos == '6':
                    numero_pedido = int(input("Numero do pedido a ser editado:\n>>> "))
                    novo_hamburguer = input("Novo Hamburguer:\n>>> ")
                    nova_quantidade_hamburguer = int(input("Nova quantidade:\n>>> "))
                    nova_bebida = input("Nova Bebida:\n>>> ")
                    nova_quantidade_bebida = int(input("Nova quantidade:\n>>> "))
                    novo_acompanhamento = input("Novo Acompanhamento:\n>>> ")
                    nova_quantidade_acompanhamento = int(input("Nova quantidade:\n>>> "))
                    nova_observacao_pedido = input("Nova observacao:\n>>> ")
                    editar_pedido(numero_pedido, novo_hamburguer, nova_quantidade_hamburguer, nova_bebida, nova_quantidade_bebida, novo_acompanhamento, nova_quantidade_acompanhamento, nova_observacao_pedido)
                
                elif opcao_pedidos == '7':
                    numero_pedido = int(input("DIGITE O NUMERO DO PEDIDO QUE DESEJA EXCLUIR:\n>>> "))
                    excluir_pedido(numero_pedido)

                elif opcao_pedidos == '8':
                    print("VOLTAR AO MENU ANTERIOR...")
                    break

                else:
                    print("OPÇÃO INVÁLIDA! Por favor, escolha uma opção válida.")

        elif escolha == '4':
            break

        else:
            print("OPÇÃO INVÁLIDA! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()

