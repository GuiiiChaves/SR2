itens_menu = {
    "hamburgueres": {
        "1": {"nome": "Hambúrguer de carne", "ingredientes": "Pão, carne, alface, tomate, queijo", "calorias": 550, "valor": 25.00},
        "2": {"nome": "Hambúrguer de frango", "ingredientes": "Pão, frango, alface, tomate, maionese", "calorias": 400, "valor": 22.00},
        "3": {"nome": "Hambúrguer vegetariano", "ingredientes": "Pão, falafel, alface, tomate, cebola roxa", "calorias": 350, "valor": 33.00}
    },
    "bebidas": {
        "1": {"nome": "Coca-Cola", "volume": "350ml", "calorias": 140, "valor": 9.00},
        "2": {"nome": "Fanta Laranja", "volume": "350ml", "calorias": 160, "valor": 8.50},
        "3": {"nome": "Água mineral", "volume": "500ml", "calorias": 0, "valor": 4.50}
    },
    "acompanhamentos": {
        "1": {"nome": "Batata frita", "porção": "150g", "calorias": 400, "valor": 17.00},
        "2": {"nome": "Salada", "porção": "200g", "calorias": 100, "valor": 10.00},
        "3": {"nome": "Anéis de cebola", "porção": "100g", "calorias": 300, "valor": 18.00}
    }
}
numero_pedido = 0
contador_pedidos = 0
pedido = {}

def mostrar_menu(categoria):
    print(f"Menu de {categoria}:")
    for numero, item in itens_menu[categoria].items():
        if categoria == "bebidas":
            print(f"{numero}: {item['nome']} - Volume: {item['volume']} - Calorias: {item['calorias']} kcal - Valor: R${item['valor']:.2f}")
        elif categoria == "hamburgueres":
            print(f"{numero}: {item['nome']} - Ingredientes: {item['ingredientes']} - Calorias: {item['calorias']} kcal - Valor: R${item['valor']:.2f}")
        elif categoria == "acompanhamentos":
            print(f"{numero}: {item['nome']} - Porção: {item['porção']} - Calorias: {item['calorias']} kcal - Valor: R${item['valor']:.2f}")

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
                    pedido[item['nome']] = {'quantidade': quantidade, 'calorias': item['calorias'], 'valor': item['valor']}
            else:
                print("Escolha inválida, tente novamente.")

    mostrar_resumo(numero_pedido)
    editar_pedido(numero_pedido)
    adicionar_comentario()

def mostrar_resumo(numero_pedido):
    print(f"\nResumo do pedido nº {numero_pedido}:")
    total_calorias = 0
    total_valor = 0
    for i, (item, detalhes) in enumerate(pedido.items(), 1):
        total_calorias += detalhes['calorias'] * detalhes['quantidade']
        total_valor += detalhes['valor'] * detalhes['quantidade']
        print(f"{i}. {detalhes['quantidade']}x {item} - Calorias: {detalhes['calorias']} kcal - Valor: R${detalhes['valor'] * detalhes['quantidade']:.2f}")
    print(f"Total de calorias do pedido: {total_calorias} kcal")
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
                                pedido[item['nome']] = {'quantidade': quantidade, 'calorias': item['calorias'], 'valor': item['valor']}
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
