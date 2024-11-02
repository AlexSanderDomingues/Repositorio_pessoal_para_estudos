import random
from random import choice

print('-'*45)
print('Bem-vindo ao Jogo Pedra, Papel e Tesoura!!')
print('-'*45)
escolhausu = input('Voce escolhe ? ').capitalize()
print('Voce escolheu: {}'.format(escolhausu))
escolhacom = choice(['Pedra','Papel','Tesoura'])
print('A maquina escolhe:',escolhacom)
if escolhausu == escolhacom:
    print('Empate!')
elif (escolhacom == 'Pedra' and escolhausu == 'Tesoura') or \
     (escolhacom == 'Tesoura' and escolhausu == 'Papel') or \
     (escolhacom == 'Papel' and escolhausu == 'Pedra'):
    print('A maquina vence!')
else:
    print('Voce venceu!')

