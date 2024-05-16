class SistemaDePedidos:
    contador_pedidos = 0  

    def __init__(self):
        self.itens_menu = {
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
                "2": {"nome": "Salada", "porção": "200g", "calorias": 100, "valor": 9.00},
                "3": {"nome": "Anéis de cebola", "porção": "100g", "calorias": 300, "valor": 18.00}
            }
        }
        self.pedido = {}
        self.comentario = ""

    def mostrar_menu(self, categoria):
        print(f"Menu de {categoria}:")
        for numero, item in self.itens_menu[categoria].items():
            if categoria == "bebidas":
                print(f"{numero}: {item['nome']} - Volume: {item['volume']} - Calorias: {item['calorias']} kcal - Valor: R${item['valor']:.2f}")
            elif categoria == "hamburgueres":
                print(f"{numero}: {item['nome']} - Ingredientes: {item['ingredientes']} - Calorias: {item['calorias']} kcal - Valor: R${item['valor']:.2f}")
            elif categoria == "acompanhamentos":
                print(f"{numero}: {item['nome']} - Porção: {item['porção']} - Calorias: {item['calorias']} kcal - Valor: R${item['valor']:.2f}")

    def fazer_pedido(self):
        SistemaDePedidos.contador_pedidos += 1
        numero_pedido = SistemaDePedidos.contador_pedidos
        print(f"Pedido nº {numero_pedido}\n")

        for categoria in self.itens_menu:
            self.mostrar_menu(categoria)
            while True:
                escolha = input(f"Escolha um item de {categoria} ou digite 's' para sair: ")
                if escolha == 's':
                    break
                if escolha in self.itens_menu[categoria]:
                    quantidade = int(input("Digite a quantidade: "))
                    item = self.itens_menu[categoria][escolha]
                    if item['nome'] in self.pedido:
                        self.pedido[item['nome']]['quantidade'] += quantidade
                    else:
                        self.pedido[item['nome']] = {'quantidade': quantidade, 'calorias': item['calorias'], 'valor': item['valor']}
                else:
                    print("Escolha inválida, tente novamente.")

        self.mostrar_resumo(numero_pedido)
        self.editar_pedido(numero_pedido)
        self.adicionar_comentario()

    def mostrar_resumo(self, numero_pedido):
        print(f"\nResumo do pedido nº {numero_pedido}:")
        total_calorias = 0
        total_valor = 0
        for item, detalhes in self.pedido.items():
            total_calorias += detalhes['calorias'] * detalhes['quantidade']
            total_valor += detalhes['valor'] * detalhes['quantidade']
            print(f"{detalhes['quantidade']}x {item} - Calorias: {detalhes['calorias']} kcal - Valor: R${detalhes['valor'] * detalhes['quantidade']:.2f}")
        print(f"Total de calorias do pedido: {total_calorias} kcal")
        print(f"Valor total do pedido: R${total_valor:.2f}")

    def editar_pedido(self, numero_pedido):
        while True:
            resposta = input("Deseja alterar algum item do pedido? (S/N): ")
            if resposta.upper() == "S":
                print("Itens no pedido:")
                for i, (item, detalhes) in enumerate(self.pedido.items(), start=1):
                    print(f"{i}. {item} - Quantidade: {detalhes['quantidade']}x - Calorias: {detalhes['calorias']} kcal - Valor: R${detalhes['valor'] * detalhes['quantidade']:.2f}")
                opcao = input("Digite '1' para alterar quantidade, '2' para excluir, ou '3' para adicionar outro item: ")
                if opcao == "1":
                    indice_item = int(input("Digite o número do item que deseja alterar: "))
                    if 1 <= indice_item <= len(self.pedido):
                        item_selecionado = list(self.pedido.keys())[indice_item - 1]
                        nova_quantidade = int(input("Digite a nova quantidade desejada: "))
                        self.pedido[item_selecionado]['quantidade'] = nova_quantidade
                    else:
                        print("Número inválido.")
                elif opcao == "2":
                    indice_item = int(input("Digite o número do item que deseja excluir: "))
                    if 1 <= indice_item <= len(self.pedido):
                        item_selecionado = list(self.pedido.keys())[indice_item - 1]
                        del self.pedido[item_selecionado]
                    else:
                        print("Número inválido.")
                elif opcao == "3":
                    for categoria in self.itens_menu:
                        self.mostrar_menu(categoria)
                        while True:
                            escolha = input(f"Escolha um item de {categoria} ou digite 's' para sair: ")
                            if escolha == 's':
                                break
                            if escolha in self.itens_menu[categoria]:
                                quantidade = int(input("Digite a quantidade: "))
                                item = self.itens_menu[categoria][escolha]
                                if item['nome'] in self.pedido:
                                    self.pedido[item['nome']]['quantidade'] += quantidade
                                else:
                                    self.pedido[item['nome']] = {'quantidade': quantidade, 'calorias': item['calorias'], 'valor': item['valor']}
                            else:
                                print("Escolha inválida, tente novamente.")
                else:
                    print("Opção inválida.")
                self.mostrar_resumo(numero_pedido)
            else:
                print("Pedido finalizado.")
                return

    def adicionar_comentario(self):
        resposta = input("Deseja adicionar um comentário ao pedido? (S/N): ")
        if resposta.upper() == "S":
            self.comentario = input("Digite seu comentário: ")
        print("Obrigado por fazer seu pedido!")

if __name__ == "__main__":
    sistema = SistemaDePedidos()
    sistema.fazer_pedido()
