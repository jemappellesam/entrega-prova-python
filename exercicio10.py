library = []
controle = True


def add_book(library, title, author):
    objeto = {
        "titulo ": title,
        "autor": author
    }
    library.append(objeto)

def list_books(library):
    if len(library >0):

     print(library)
     else:
        print("Não há livros")

def  find_book_by_title(library, title):
     controle = 0
     while(controle < len(library)):
        livro = library[controle].titulo
        if(livro == title):
            print(library[controle])
            controle = len(library)
        else:
             controle = contrale + 1    


def menu():
    print("Digite 1 para adicionar um livro")
    print("Digite 2 para listar todos os livros")
    print("Digite 3 para buscar um livro por título")
    print("Digite 4 para sair")
    opcao = input()
    if opcao == str(1):
        livro = input('Digite o título do livro a ser adicionado')
        autor = input('Digite o autor do livro')
        add_book(library, livro, autor)
    elif opcao == str(2):
        list_books(library)
    elif opcao == str(3):
        titulo  = input("Digite o título do livro a ser buscado")
        find_book_by_title(library, titulo)
    elif opcao == str(4):
        print('Adeus')
        controle = False


while (controle):
    menu()

