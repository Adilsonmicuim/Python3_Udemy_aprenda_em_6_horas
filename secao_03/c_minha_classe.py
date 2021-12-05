class Pessoa:

    def __init__(self, nome, apelido, ano):
        self.nome = nome
        self.apelido = apelido
        self.ano = ano

    def __str__(self):
        return 'Nome: %s, Apelido: %s, Ano: %s' % \
               (self.nome, self.apelido, self.ano)


livro_01 = Pessoa('Adilson', 'Micuim', 1984)
livro_02 = Pessoa('Mandrik', 'Dick', 2005)

print(livro_01)
print(livro_02)
print(livro_02.nome)
print(livro_02.apelido)
