from Autor import Autor
from Livro import Livro

class Biblioteca:
    def __init__(self):
        self.autores = []
        self.livros = []

    # ---------- AUTOR ----------
    def cadastrar_autor(self, nome):
        autor = Autor(nome)
        self.autores.append(autor)
        print("Autor cadastrado com sucesso!")

    def listar_autores(self):
        if not self.autores:
            print("Nenhum autor cadastrado.")
            return
        for autor in self.autores:
            print(autor)

    def buscar_autor_por_id(self, autor_id):
        for autor in self.autores:
            if autor.id == autor_id:
                return autor
        return None

    # ---------- LIVRO ----------
    def cadastrar_livro(self, titulo, autor_id, ano, valor, numero):
        autor = self.buscar_autor_por_id(autor_id)
        if not autor:
            print("Autor não encontrado.")
            return

        livro = Livro(titulo, autor, ano, valor, numero)
        self.livros.append(livro)
        print("Livro cadastrado com sucesso!")

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return
        for livro in self.livros:
            print(livro)
