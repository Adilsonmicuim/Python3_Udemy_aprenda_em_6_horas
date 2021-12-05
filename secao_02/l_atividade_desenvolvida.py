# http://pep8online.com/checkresult

nome = input("Digite seu nome: ")

materia = input("Nome da matéria: ")

a = float(input("Digite a primeira nota: "))
b = float(input("Digite a Segunda nota: "))
c = float(input("Digite a Terceira nota: "))
d = float(input("Digite a Quarta nota: "))

media = (a + b + c + d) / 4

if media < 7:
    print("%s sua média em %s foi: %f" %
          (nome, materia, media), ", Situação: REPROVADO")
else:
    print("%s sua média em %s foi: %f" %
          (nome, materia, media), ", Situação: APROVADO")

