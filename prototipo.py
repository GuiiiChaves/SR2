class OrderSystem:
    def __init__(self):
        self.profile_created = False
        self.order = {}
        self.usuarios = {}

    def cadastrar_usuario(self, cpf, nome, numero_telefone, genero, idade, observacoes):
        if cpf not in self.usuarios:
            self.usuarios[cpf] = {"CPF": cpf, "Nome": nome, "Numero": numero_telefone, "Gênero": genero, "Idade": idade, "Observações": observacoes}
            print("Usuário cadastrado com sucesso!")
        else:
            print("CPF já cadastrado!")

    def login(self, cpf):
        if cpf in self.usuarios and cpf == self.usuarios[cpf]["CPF"]:
            print("Login bem sucedido! Bem-vindo,", self.usuarios[cpf]["Nome"])
        else:
            print("CPF não cadastrado ou incorreto!")

    def entrar_como_visitante(self):
        print("Início de atendimento!")

    def main(self):
        while True:
            print("1. Cadastrar")
            print("2. Login")
            print("3. Entrar como visitante")
            print("4. Sair")
            choice = input("Escolha uma opção: ")

            if choice == "1":
                cpf = input("Digite seu CPF: ")
                nome = input("Digite seu Nome: ")
                numero_telefone = input("Digite seu número de telefone: ")
                genero = input("Digite seu gênero: ")
                idade = int(input("Digite sua idade: "))
                observacoes = input("Se você tiver coisas que não pode comer: ")
                self.cadastrar_usuario(cpf, nome, numero_telefone, genero, idade, observacoes)

            elif choice == "2":
                cpf = input("Digite seu CPF: ")
                self.login(cpf)
                break

            elif choice == "3":
                self.entrar_como_visitante()
                print("Você entrou como visitante!")
                break

            elif choice == "4":
                print("Saindo...")
                break

            else:
                print("Opção inválida!")

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
        self.main()
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

order_system = OrderSystem()
order_system.run()
