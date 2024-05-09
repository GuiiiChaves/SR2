usuarios = {}

def cadastrar_usuario(nome, email, password):
    if email not in usuarios:
        usuarios[email] = {"nome": nome, "senha": password}
        print("Usuário cadastrado com sucesso!")
    else:
        print("E-mail já cadastrado!")

def login(email, password):
    if email in usuarios and usuarios[email]["senha"] == password:
        print("Login bem sucedido! Bem-vindo,", usuarios[email]["nome"])
    else:
        print("E-mail ou senha incorretos!")

def entrar_como_visitante():
    print("Você entrou como visitante.")
    # Aqui você pode adicionar qualquer lógica específica para visitantes, se necessário.

def main():
    while True:
        print("\n1. Cadastrar")
        print("2. Login")
        print("3. Entrar como visitante")
        print("4. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            nome = input("Digite seu nome: ")
            email = input("Digite seu e-mail: ")
            password = input("Digite a senha: ")
            cadastrar_usuario(nome, email, password)
        elif choice == "2":
            email = input("Digite seu e-mail: ")
            password = input("Digite a senha: ")
            login(email, password)
        elif choice == "3":
            entrar_como_visitante()
        elif choice == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
