'''
Criar uma função que me lembre a parar de estudar e fazer uma pausa a cada 2h
Trabalho inicia de 8h as 12
'''
import webbrowser
import time

intervalos = 2  # Vai abrir duas vezes o navegador
contador = 0
print('O programa de controle de descanso foi ativado ')

while contador < intervalos:
    time.sleep(10)  # Tempo em segundos para abrir a URL
    webbrowser.open('https://www.youtube.com/watch?v=JRVD-pndqY0')
    contador = contador + 1
