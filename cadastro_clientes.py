import os
import json
from time import sleep

arquivo2 = os.path.join(os.path.dirname(__file__), 'cadastro_clientes.json')

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
        print("=" *60)
        print("LISTA DE USUÁRIOS:")
        print("-" *60)
        for usuario in usuarios:
            print("*" *60)
            print(f"CPF: {usuario['CPF']}, NOME: {usuario['nome']}, NUMERO: {usuario['numero']}, OBSERVACOES: {usuario['observacoes']}, IDADE: {usuario['idade']}")
            print("*" *60)
            print("=" *60)
