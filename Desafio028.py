from random import randint
from time import sleep
comp = randint(0, 5)  # Faz o computador "Pensar"
print('-=' * 40, '\n Vou pensar em um número entre 0 e 5. tente adivinhar qual.')
print('-=' * 40)
player = int(input('Eu chuto o número: '))  # o Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(1.5)
if comp == player:
    print('Aff, você acertou o número.')
else:
    print(f'Haha, eu Ganhei! Eu pensei no número {comp} e não no {player}!')
