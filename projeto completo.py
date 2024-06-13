import json
import os
from time import sleep

arquivo = os.path.join(os.path.dirname(__file__), 'codigo_produto.json')
arquivo2 = os.path.join(os.path.dirname(__file__), 'cadastro_clientes.json')
arquivo3 = os.path.join(os.path.dirname(__file__), 'cardapio.json')

class Cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'

def verificar_arquivo_clientes():
    if not os.path.exists(arquivo2):
        with open(arquivo2, 'w') as file:
            json.dump([], file) 
            
def cadastrar_usuario(cpf, nome, numero, observacoes, idade):
    with open(arquivo2, 'r') as file:
        usuarios = json.load(file)

    usuarios.append({'CPF': cpf, 'nome': nome, 'numero': numero, 'observacoes': observacoes, 'idade': idade})

    with open(arquivo2, 'w') as file:
        json.dump(usuarios, file, indent=4)
    print("USUARIO CADASTRADO COM SUCESSO!")

def login(cpf):
    with open(arquivo2, 'r') as file:
        usuarios = json.load(file)

    for usuario in usuarios:
        if usuario['CPF'] == cpf:
            return True
        
        return False
        
def entrar_como_visitante():
    visitante = input("ESCREVA SEU NOME: ")
    print("Início de atendimento!\n OLÁ ", visitante)

def editar_usuario(cpf_usuario, nome_novo, numero_novo, observacoes_novas, nova_idade):
    with open(arquivo2, 'r') as file:
        usuarios = json.load(file)

    for usuario in usuarios:
        if usuario['CPF'] == cpf_usuario:
            usuario['nome'] = nome_novo
            usuario['numero'] = numero_novo
            usuario['observacoes'] = observacoes_novas
            usuario['idade'] = nova_idade
            break

    with open(arquivo2, 'w') as file:
        json.dump(usuarios, file, indent=4)
    print("USUÁRIO ATUALIZADO COM SUCESSO!")

def excluir_usuario(cpf):
    with open(arquivo2, 'r') as file:
        usuarios = json.load(file)

    for usuario in usuarios:  
        if usuario['CPF'] == cpf:
            usuarios.remove(usuario)

    with open(arquivo2, 'w') as f:
        json.dump(usuarios, f, indent=4)
    print("USUÁRIO EXCLUÍDO COM SUCESSO!")

def buscar_usuario(cpf):
    with open(arquivo2, 'r') as file:
        usuarios = json.load(file)
    
    encontrado = False

    for usuario in usuarios:
        if usuario['CPF'] == cpf:
            print(f"CPF: {usuario['CPF']}, NOME: {usuario['nome']}, NUMERO: {usuario['numero']}, OBSERVACOES: {usuario['observacoes']}, IDADE: {usuario['idade']}")
            encontrado = True
            
    if not encontrado:
            print("NENHUM USUÁRIO ENCONTRADO!")      

def listar_usuarios():
    with open(arquivo2, 'r') as file:
        usuarios = json.load(file)

    if usuarios:
        print("=" *80)
        print("LISTA DE USUÁRIOS:")
        print("-" *80)
        for usuario in usuarios:
            print("*" *80)
            print(f"CPF: {usuario['CPF']}, NOME: {usuario['nome']}, NUMERO: {usuario['numero']}, OBSERVACOES: {usuario['observacoes']}, IDADE: {usuario['idade']}")
            print("*" *80)
            print("=" *80)      

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

def buscar_pedido (numero_pedido):
    with open(arquivo3, 'r') as file_:
        pedidos = json.load(file_)
    
    encontrado = False

    for pedido in pedidos:
        if pedido['Numero do pedido'] == numero_pedido:
            print(f"NOME: {pedido['Nome']}, NUMERO DO PEDIDO: {pedido['Numero do pedido']}, HAMBURGUER: {pedido['Hamburguer']}, QUANTIDADE HAMBURGUER: {pedido['Quantidade hamburguer']}, BEBIDA: {pedido['Bebida']}, QUANTIDADE BEBIDA: {pedido['Quantidade bebida']}, ACOMPANHAMENTO: {pedido['Acompanhamento']}, QUANTIDADE ACOMPANHAMENTO: {pedido['Quantidade acompanhamento']}, OBSERVACAO: {pedido['Observacao do pedido']}")
            encontrado = True
    if not encontrado:
            print("NENHUM PEDIDO ENCONTRADO")

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

def menu_usuarios():
    print("\nMENU DE USUÁRIOS!")
    print("1. CADASTRAR USUÁRIO")
    print("2. LOGIN")
    print("3. ENTRAR COMO VISITANTE")
    print("4. EDITAR PERFIL")
    print("5. EXCLUIR PERFIL")
    print("6. LISTAR USUARIOS")
    print("7. BUSCAR PERFIL")
    print("8. VOLTAR AO MENU ANTERIOR")

def menu_produtos():
    print("\nMENU DE PRODUTOS!")
    print("1. CADASTRAR PRODUTO")
    print("2. LISTAR PRODUTOS")
    print("3. BUSCAR PRODUTO")
    print("4. EDITAR PRODUTO")
    print("5. EXCLUIR PRODUTO")
    print("6. VOLTAR AO MENU ANTERIOR")

def menu_pedidos():
    print("\n========== CARDÁPIO! ==========")
    print("1. HAMBURGUERES")
    print("2. BEBIDAS")
    print("3. ACOMPANHAMENTOS")
    print("4. FINALIZAR PEDIDO")
    print("5. LISTAR PEDIDOS")
    print("6. EDITAR PEDIDO")
    print("7. EXCLUIR PEDIDO")
    print("8. BUSCAR PEDIDO") 
    print("9. VOLTAR AO MENU ANTERIOR")


def menu_hamburguer():
    print("1. CLASSICO (780cal) => INGREDIENTES: pao brioche; hamburguer bovino(180g); queijo cheddar; alface; tomate; cebola; valor --> R$25.00")
    print("2. BACON MANIA (830cal) => INGREDIENTES: pao australiano; hamburguer angus(180g); queijo mussarela; bacon; alface; tomate; cebola; molho barbecue; valor --> R$30.00")
    print("3. FRANGO GRELHADO (530cal) => INGREDIENTES: pao brioche; carne de porco(180g); queijo gruyère; bacon; picles; molho mostarda; valor --> R$28.00")
    print("4. PORCO C/ QUEIJO (860cal) => INGREDIENTES: pao integral; peito de frango grelhado(180g); queijo prato; presunto; tomate; alface; ketchup; valor --> R$27.00")
    print("5. EXPLOSAO DE SABOR (855cal) => INGREDIENTES: pao australiano; hamburguer angus(180g); queijo cheddar; bacon; alface; tomate; maionese; valor --> R$32.00")

def menu_bebida():
    print("1. Água com gás => cal: 0, valor --> R$5.00")
    print("2. Água sem gás => cal: 0, valor --> R$4.00")
    print("3. Suco de Laranja => cal: 120, valor --> R$8.00")
    print("4. Suco de Acerola => cal: 100, valor --> R$8.00")
    print("5. Suco de Caja => cal: 110, valor --> R$8.50")
    print("6. Guarana Antartica => cal: 150, valor --> R$10.00")
    print("7. Coca-Cola => cal: 140, valor --> R$10.00")
    print("8. Fanta Laranja => cal: 160, valor --> R$10.00")

def menu_acompanhamento():
    print("1. Batata Rústica => porção: 100g, cal: 200g, valor --> R$20.00")
    print("2. Batata Canoa => porção: 100g cal: 220, valor --> R$20.00")
    print("3. Batata Frita => porção: 100g, cal: 300, valor --> R$15.00")
    print("4. Batata Bacon => porção: 100g, cal: 350, valor --> R$25.00")
    print("5. Onion Rings => porção: 100g, cal: 250, valor --> R$20.00")


def main():
    verificar_arquivo_produto()
    verificar_arquivo_clientes()
    verificar_arquivo_pedidos()
    
    contador_pedidos = 0

    while True:
        menu_inicial()
        escolha = int(input("ESCOLHA UMA OPÇÃO:\n>>> "))

        match(escolha):
            case 1:
                while True:
                    menu_usuarios()
                    opcao_usuario = input("ESCOLHA UMA OPÇÃO:\n>>> ")

                    if opcao_usuario == "1":
                        cpf = input("Digite seu CPF: ")
                        nome = input("Digite seu Nome: ")
                        numero_telefone = input("Digite seu número de telefone: ")
                        observacoes = input("Observacao: ")
                        idade = int(input("Digite sua idade: "))
                        cadastrar_usuario(cpf, nome, numero_telefone, observacoes, idade)

                    elif opcao_usuario == "2":
                        cpf = input("Digite seu CPF: ")
                        usuario = login(cpf)
                        if(usuario):
                            print("LOGIN EFETUADO COM SUCESSO!")
                            
                        else:
                            print("USURIO NO ENCONTRADO!")
                        break

                    elif opcao_usuario == "3":
                        entrar_como_visitante()
                        print("Você entrou como visitante!")
                        break

                    elif opcao_usuario == "4":
                        cpf_usuario = input("DIGITE O CPF DA PESSOA QUE SERA ATUALIZADO:\n>>>")
                        nome_novo = input("DIGITE O NOVO NOME:\n>>> ")
                        numero_novo = input("DIGITE O NOVO NUMERO:\n>>> ")
                        observacoes_novas = input("DIGITE A NOVA OBSERVACAO:\n>>> ")
                        nova_idade = int(input("DIGITE A NOVA IDADE:\n>>> "))              
                        editar_usuario(cpf_usuario, nome_novo, numero_novo, observacoes_novas, nova_idade)
                    
                    elif opcao_usuario == "5":
                        cpf = input("DIGITE O CPF QUE DESEJA EXCLUIR:\n>>> ")
                        excluir_usuario(cpf)
                        
                    elif opcao_usuario == "6":
                        listar_usuarios()

                    elif opcao_usuario == "7":
                        cpf = input("DIGITE O CPF DO USUÁRIO:\n>>>")
                        buscar_usuario(cpf)
                        
                    elif opcao_usuario == "8":
                        print("VOLTAR AO MENU ANTERIOR...")
                        sleep(3)
                        break

                    else:
                        print("Opção inválida!")

            case 2:
                while True:
                    menu_produtos()
                    opcao_produtos = input("ESCOLHA UMA OPÇÃO:\n>>> ")

                    if opcao_produtos == "1":
                        codigo_produto = input("CODIGO DO PRODUTO:\n>>> ")
                        tipo_produto = input("TIPO DO PRODUTO:\n>>> ")
                        cadastrar_produto(codigo_produto, tipo_produto)
                        
                    elif opcao_produtos == "2":
                        listar_produtos()

                    elif opcao_produtos == "3":
                        codigo_produto = input("CODIGO DO PRODUTO: ")
                        buscar_produto(codigo_produto)

                    elif opcao_produtos == "4":
                        codigo_produto_antigo = input("DIGITE O CODIGO A SER MUDADO:\n>>> ")
                        novo_codigo_produto = input("DIGITE O NOVO CODIGO DO PRODUTO:\n>>> ")
                        novo_tipo_produto = input("DIGITE O TIPO DO PRODUTO:\n>>> ")
                        atualizar_produto(codigo_produto_antigo, novo_codigo_produto, novo_tipo_produto)

                    elif opcao_produtos == "5":
                        codigo_produto = input("DIGITE O CODIGO PARA SER EXCLUÍDO:\n>>> ")
                        excluir_produto(codigo_produto)

                    elif opcao_produtos == "6":
                        print("VOLTAR AO MENU ANTERIOR...")
                        sleep(3)
                        break

                    else:
                        print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

            case 3:  
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
                        '5': 'ONION RINGS'
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
                            numero_pedido = int(input("NUMERO DO PEDIDO:\n>>> "))
                            menu_hamburguer()
                            opcao_hamburguer = input("ESCOLHA UMA NOVA OPÇÃO DE HAMBURGUER:\n>>> ")
                            novo_hamburguer = hamburguer_nome.get(opcao_hamburguer, "OPCAO INVALIDA!")
                            nova_quantidade_hamburguer = int(input("NOVA QUANTIDADE:\n>>> "))
                            menu_bebida()
                            opcao_bebida = input("ESCOLHA UMA NOVA OPÇÃO DE BEBIDA:\n>>> ")
                            nova_bebida = bebida_nome.get(opcao_bebida, "OPCAO INVALIDA!")
                            nova_quantidade_bebida = int(input("Nova quantidade:\n>>> "))
                            menu_acompanhamento()
                            opcao_acompanhamento = input("ESCOLHA UMA NOVA OPÇÃO DE ACOMPANHAMENTO:\n>>> ") 
                            novo_acompanhamento = acompanhamento_nome.get(opcao_acompanhamento, "OPCAO INVALIDA!")
                            nova_quantidade_acompanhamento = int(input("NOVA QUANTIDADE:\n>>> "))
                            nova_observacao_pedido = input("NOVA OBSERVACAO:\n>>> ")
                            editar_pedido(numero_pedido, novo_hamburguer, nova_quantidade_hamburguer, nova_bebida, nova_quantidade_bebida, novo_acompanhamento, nova_quantidade_acompanhamento, nova_observacao_pedido)
                                          
                        elif opcao_pedidos == '7':
                            numero_pedido = int(input("DIGITE O NUMERO DO PEDIDO QUE DESEJA EXCLUIR:\n>>> "))
                            excluir_pedido(numero_pedido)

                        elif opcao_pedidos == '8':
                            numero_pedido = int(input("DIGITE O NUMERO DO PEDIDO:\n>>> "))
                            buscar_pedido(numero_pedido)

                        elif opcao_pedidos == '9':
                            print("VOLTAR AO MENU ANTERIOR...")
                            sleep(3)
                            break

                        else:
                            print("OPÇÃO INVÁLIDA! Por favor, escolha uma opção válida.")

            case 4:
                print("🚀 SAINDO...")
                sleep(3)
                break

            case __:
                print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()
