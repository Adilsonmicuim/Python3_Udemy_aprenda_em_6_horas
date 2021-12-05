# import a_funcao.modulo_media_escolar
#
# a = float(input("Primeira nota: "))
# b = float(input("Segunda nota: "))
# c = float(input("Terceira nota: "))
# d = float(input("Quarta nota: "))
#
# media2 = a_funcao.modulo_media_escolar.media_escolar(a, b, c, d)
# print(media2)


# Forma mais correta para importar pacotes
from a_funcao.modulo_media_escolar import media_escolar

e = float(input("Primeira nota: "))
f = float(input("Segunda nota: "))
g = float(input("Terceira nota: "))
h = float(input("Quarta nota: "))

media3 = media_escolar(e, f, g, h)
print(media3)
