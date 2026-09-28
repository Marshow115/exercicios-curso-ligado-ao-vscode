
biblioteca = {}

def adicionar():
    """Adiciona um livro à biblioteca.
    """
    livro = {}
    livro["titulo"] = input("Adicione um título: ")    
    livro["autor"] = input("Quem é o autor? ")
    livro["disponivel"] = True


    biblioteca[livro["titulo"]] = livro
    print("Livro adicionado!")


def estante():
    if biblioteca:
        print("\nLivros disponíveis:")

        for titulo, livro in biblioteca.items():
            print(f"{titulo} - {livro['autor']} ({'Disponível' if livro['disponivel'] else 'Indisponível'})")
    else:
        print("A biblioteca está vazia.")


def pesquisar():
    """Pesquisa um livro na biblioteca.
    """
    titulo = input("Qual livro está procurando? ")

    if titulo in biblioteca:
        print(f"{titulo} - {biblioteca[titulo]['autor']} ({'Disponível' if biblioteca[titulo]['disponivel'] else 'Indisponível'})")
    else:
        print("Livro não encontrado.")


def emprestar():
    """Empresta um livro da biblioteca.
    """
    titulo = input("Qual livro você quer emprestar? ")

    if titulo in biblioteca:
        if biblioteca[titulo]["disponivel"]:
            biblioteca[titulo]["disponivel"] = False
            print("Empréstimo feito com sucesso!")
        else:
            print("Esse livro não está disponível.")
    else:
        print("Livro não encontrado.")


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
