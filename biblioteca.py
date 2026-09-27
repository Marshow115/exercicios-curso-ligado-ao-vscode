
biblioteca = {}


def adicionar():
    titulo = input("Adicione um título: ")
    autor = input("Quem é o autor? ")

    biblioteca[titulo] = autor
    print("Livro adicionado!")


def estante():
    if biblioteca:
        print("\nLivros disponíveis:")

        for titulo, autor in biblioteca.items():
            print(f"{titulo} - {autor}")
    else:
        print("A biblioteca está vazia.")


def pesquisar():
    titulo = input("Qual livro está procurando? ")

    if titulo in biblioteca:
        print(f"{titulo} - {biblioteca[titulo]}")
    else:
        print("Livro não encontrado.")


def emprestar():
    titulo = input("Qual livro você quer emprestar? ")

    if titulo in biblioteca:
        print("Empréstimo feito com sucesso!")
    else:
        print("Esse livro não está disponível.")


while True:
    print("\n--- BIBLIOTECA ---")
    print("1. Adicionar um livro")
    print("2. Ver estante")
    print("3. Pesquisar um livro")
    print("4. Emprestar um livro")
    print("5. Fechar a biblioteca")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        adicionar()

    elif escolha == "2":
        estante()

    elif escolha == "3":
        pesquisar()

    elif escolha == "4":
        emprestar()

    elif escolha == "5":
        print("Até a próxima!")
        break

    else:
        print("Opção inválida.")
