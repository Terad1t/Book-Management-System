class Livro:
    _contador_id = 1

    def __init__(self, titulo, autor, ano, valor, numero):
        self.id = Livro._contador_id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.valor = valor
        self.numero = numero
        Livro._contador_id += 1

    def __repr__(self):
        return (
            f"[{self.id}] {self.titulo} | "
            f"Autor: {self.autor.nome} | "
            f"Ano: {self.ano} | "
            f"R$ {self.valor:.2f} | Nº {self.numero}"
        )
