import random

tentavivas = 7
jogadas = 1
chute = 0

numero_secreto = random.randint(0, 100)

while tentavivas <= 7:
    chute = int(input("Digite um número entre 0 e 100: "))
    if chute > numero_secreto:
        print("Você ERROU")
    else:
        print("Você ACERTOU")
