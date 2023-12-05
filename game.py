from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('\33[33m=-\33[m'*10)
print('''Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
print('\33[33m=-\33[m'*10)

jogador = int(input('Qual é a sua jogada?'))
print('1')
sleep(0.5)
print('2')
sleep(0.5)
print('3')
sleep(0.5)
print('JÁ!')

print('\33[35m~-=\33[m'*10)
print('\33[31mComputador\33[m jogou {}'.format(itens[computador]))
print('\33[32mJogador\33[m jogou {}'.format(itens[jogador]))
print('\33[35m~-=\33[m'*10)

if computador == 0: #PEDRA
    if jogador == 0:
        print('\33[33mEMPATE\33[m')
    elif jogador == 1:
        print('\33[32mJOGADOR VENCE\33[m')
    elif jogador == 2:
        print('\33[31mCOMPUTADOR VENCE\33[m')
    else:
        print('\33[31mJOGADA INVÁLIDA!\33[m')
elif computador == 1: #PAPEL
    if jogador == 0:
        print('\33[31mCOMPUTADOR VENCE\33[m')
    elif jogador == 1:
        print('\33[33mEMPATE\33[m')
    elif jogador == 2:
        print('\33[32mJOGADOR VENCE\33[m')
    else:
        print('\33[31mJOGADA INVÁLIDA!\33[m')
elif computador == 2: #TESOURA
    if jogador == 0:
        print('\33[32mJOGADOR VENCE\33[m')
    elif jogador == 1:
        print('\33[31mCOMPUTADOR VENCE\33[m')
    elif jogador == 2:
        print('\33[33mEMPATE\33[m')
    else:
        print('\33[31mJOGADA INVÁLIDA!\33[m')
