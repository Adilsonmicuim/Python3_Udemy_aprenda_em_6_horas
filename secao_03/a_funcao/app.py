import modulo_media_escolar

media = modulo_media_escolar.media_escolar(8, 9, 7, 9)
print(media)

print("#######################################################")
a = float(input("Primeira nota: "))
b = float(input("Segunda nota: "))
c = float(input("Terceira nota: "))
d = float(input("Quarta nota: "))

media2 = modulo_media_escolar.media_escolar(a, b, c, d)
print(media2)
