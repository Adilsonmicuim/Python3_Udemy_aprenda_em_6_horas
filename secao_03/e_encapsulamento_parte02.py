class Livro:

    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.autor = autor

    # Encapsulamento
    @property  # Significa GET
    def titulo(self):
        return self.__titulo

    # Encapsulamento
    @titulo.setter  # Significa SET
    def titulo(self, titulo):
        self.__titulo = titulo


livro1 = Livro('Curso de Python', 'Alcimar Costa')
print(livro1.autor)
print(livro1.titulo)
livro1.titulo = 'Novo titulo'
print(livro1.titulo)
