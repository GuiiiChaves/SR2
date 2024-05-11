class OrderSystem:
    def __init__(self):
        self.profile_created = False
        self.order = {}

    def create_profile(self):
        print("Criação de perfil, com base em restrições/alimentares e preferências")
        response = input("Você deseja criar um perfil? (SIM/NAO): ")
        if response.upper() == "SIM":
            self.profile_created = True
            print("Perfil criado com sucesso!")
        else:
            print("Perfil pré-definido")

    def show_menu(self, menu_type):
        print(f"Menu de {menu_type}:")
        if menu_type.lower() == "hamburgueres":
            self.menu_items = {
                "1": "Hamburguer de carne",
                "2": "Hamburguer de frango",
                "3": "Hamburguer vegetariano"
            }
        elif menu_type.lower() == "bebidas":
            self.menu_items = {
                "1": "Coca-Cola",
                "2": "Fanta Laranja",
                "3": "Água mineral"
            }
        elif menu_type.lower() == "acompanhamentos":
            self.menu_items = {
                "1": "Batata frita",
                "2": "Salada",
                "3": "Anéis de cebola"
            }
        else:
            self.menu_items = {}

        for item_number, item_name in self.menu_items.items():
            print(f"{item_number}: {item_name}")

        response = input(f"Você deseja pedir algo mais? (SIM/NAO): ")
        if response.upper() == "SIM":
            return True
        else:
            return False

    def edit_ingredients(self):
        print("Edite seus ingredientes aqui, podendo retirar e adicionar novos.")
        # Add ingredient editing logic here

    def save_order(self):
        print("Pedido salvo!")
        print("Resumo do pedido!")

    def leave_comment(self):
        print("Deseja deixar um comentário?")
        response = input("Faça um comentário!: ")
        print("OBRIGADO POR COMPRAR CONOSCO!")

    def run(self):
        self.create_profile()
        if self.profile_created:
            while True:
                print("Home")
                print("Produtos")
                response = input("Você deseja pedir algo? (SIM/NAO): ")
                if response.upper() == "SIM":
                    if self.show_menu("hamburgueres"):
                        self.edit_ingredients()
                    if self.show_menu("bebidas"):
                        pass
                    if self.show_menu("acompanhamentos"):
                        pass
                    self.save_order()
                    break
                else:
                    break
        self.leave_comment()

if __name__ == "__main__":
    order_system = OrderSystem()
    order_system.run()