usuarios = {}

def cadastrar_usuario(cpf, nome, numero_telefone, genero, idade, observacoes):
    if cpf not in usuarios:
        usuarios[cpf] = {"CPF": cpf, "Nome": nome, "Numero": numero_telefone, "Gênero": genero, "Idade": idade, "Observações": observacoes}
        print("Usuário cadastrado com sucesso!")
    else:
        print("CPF já cadastrado!")

def login(cpf):
    if cpf in usuarios and usuarios[cpf] == cpf:
        print("Login bem sucedido! Bem-vindo,", usuarios["cpf"])
    else:
        print("E-mail ou senha incorretos!")

def main():
    while True:
        print("\n1. Cadastrar")
        print("2. Login")
        print("3. Entrar como visitante")
        print("4. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            cpf = float(input("Digite seu CPF: "))
            nome = input("Digite seu Nome: ")
            numero_telefone = float(input("Digite seu numero de telefone: "))
            genero = input("Digite seu gênero: ")
            idade = int(input("Digite sua idade: "))
            observacoes = input("Se voce tiver coisas que nao pode comer: ")
            cadastrar_usuario(nome, cpf, numero_telefone, genero, idade, observacoes)

        elif choice == "2":
            cpf = float(input("Digite seu CPF: "))
            login(cpf)
            
        elif choice == "3":
            entrar_como_visitante()

        elif choice == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
