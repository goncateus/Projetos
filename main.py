import random
from faker import Faker
from database import create_tables
import models

fake = Faker('pt_BR')

def menu():
    print("\n--- Sistema de Registro de Pessoas ---")
    print("1 - Adicionar pessoa aleatória")
    print("2 - Listar pessoas")
    print("3 - Buscar pessoa por nome")
    print("4 - Atualizar pessoa")
    print("5 - Deletar pessoa")
    print("6 - Sair")

def gerar_pessoa_fake():
    return fake.name(), fake.address().replace("\n", ", "), fake.phone_number()

def main():
    create_tables()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome, endereco, telefone = gerar_pessoa_fake()
            models.adicionar_pessoa(nome, endereco, telefone)

        elif opcao == '2':
            models.listar_pessoas()

        elif opcao == '3':
            nome = input("Digite o nome para buscar: ")
            models.buscar_pessoa_por_nome(nome)

        elif opcao == '4':
            id_pessoa = int(input("Digite o ID da pessoa que deseja atualizar: "))
            nome = input("Novo nome: ")
            endereco = input("Novo endereço: ")
            telefone = input("Novo telefone: ")
            models.atualizar_pessoa(id_pessoa, nome, endereco, telefone)

        elif opcao == '5':
            id_pessoa = int(input("Digite o ID da pessoa que deseja deletar: "))
            models.deletar_pessoa(id_pessoa)

        elif opcao == '6':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

