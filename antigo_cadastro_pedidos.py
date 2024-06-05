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

fazer_pedido()
