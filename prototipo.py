class OrderSystem:
    def __init__(self):
        self.order = {}

    def entrar_como_visitante(self):
        print("Início de atendimento!")

    def main(self):
        while True:
            response = input("Você deseja pedir algo? (SIM/NÃO): ")
            if response.upper() == "SIM":
                self.select_items()
                self.save_order()
                break
            else:
                break

    def select_items(self):
        self.order = {}  
        self.select_category("hamburgueres")
        self.select_category("bebidas")
        self.select_category("acompanhamentos")

    def select_category(self, category):
        print(f"Escolha os itens de {category}:")
        if category.lower() == "Hambúrgueres":
            menu_items = {
                "1": "Hambúrguer de carne",
                "2": "Hambúrguer de frango",
                "3": "Hambúrguer vegetariano"
            }
        elif category.lower() == "Bebidas":
            menu_items = {
                "1": "Coca-Cola",
                "2": "Fanta Laranja",
                "3": "Água mineral"
            }
        elif category.lower() == "Acompanhamentos":
            menu_items = {
                "1": "Batata frita",
                "2": "Salada",
                "3": "Anéis de cebola"
            }
        else:
            menu_items = {}

        for item_number, item_name in menu_items.items():
            print(f"{item_number}: {item_name}")

        while True:
            response = input(f"Escolha um item de {category} (ou N para continuar): ")
            if response.upper() == "N":
                break
            elif response in menu_items:
                quantity = int(input("Digite a quantidade desejada: "))
                self.add_to_order(menu_items[response], quantity)
            else:
                print("Número de item inválido.")

    def add_to_order(self, item_name, quantity):
        if item_name in self.order:
            self.order[item_name]['quantity'] += quantity
        else:
            self.order[item_name] = {'quantity': quantity}

    def save_order(self):
        print("Pedido salvo!")
        self.show_summary()
        self.leave_comment()

    def show_summary(self):
        print("\nResumo do pedido:")
        for item_name, item_details in self.order.items():
            print(f"- {item_name}: {item_details['quantity']}x")

    def leave_comment(self):
        response = input("Deseja deixar um comentário? (SIM/NÃO): ")
        if response.upper() == "SIM":
            comment = input("Faça um comentário!: ")
            print("OBRIGADO POR COMPRAR CONOSCO!")
        elif response.upper() == "NAO":
            print("OBRIGADO POR COMPRAR CONOSCO!")
        else:
            print("Opção inválida!")

    def run(self):
        self.main()

order_system = OrderSystem()
order_system.run()
