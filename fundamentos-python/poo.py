# programação orientada a objetos

class LibraryBook (object):

    def __init__(self, title, author, publisher_year, call_number):
        self.title = title
        self.author = author
        self.publisher_year = publisher_year
        self.call_number = call_number
        self.checked_out = False


    def title_and_author(self):
        return f"{self.title} de {self.author}"

    def __str__(self):
        return f"{self.title} - {self.author} - {self.publisher_year}"

    def __repr__(self):
        return f"LibraryBook({self.title}, {self.call_number})"

# criando uma instância
livro1 = LibraryBook("O senhor dos anéis", "J.R.R. Tolkien", 1954, "PZ7.R79835")

# chamando os métodos
print(livro1.title_and_author())
print(livro1)
print(repr(livro1))

# acessando um atributo diretamente
print(livro1.call_number)

# herança
class Ebook (LibraryBook):

    pass


