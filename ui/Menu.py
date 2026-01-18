from Biblioteca import *

def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n=== MENU BIBLIOTECA ===")
        print("1 - Cadastrar autor")
        print("2 - Listar autores")
        print("3 - Cadastrar livro")
        print("4 - Listar livros")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do autor: ")
            biblioteca.cadastrar_autor(nome)

        elif opcao == "2":
            biblioteca.listar_autores()

        elif opcao == "3":
            if not biblioteca.autores:
                print("Cadastre um autor primeiro.")
                continue

            print("\nAutores disponíveis:")
            biblioteca.listar_autores()

            try:
                autor_id = int(input("ID do autor: "))
                titulo = input("Título do livro: ")
                ano = int(input("Ano de publicação: "))
                valor = float(input("Valor do livro: "))
                numero = int(input("Número do livro: "))

                biblioteca.cadastrar_livro(
                    titulo, autor_id, ano, valor, numero
                )
            except ValueError:
                print("Erro: dados inválidos.")

        elif opcao == "4":
            biblioteca.listar_livros()

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida.")
