import random
maquina = random.randint (0,10)

print ('Sou seu computador...')
print ('Acabei de pensar em um numero entre 0 e 10.')
print ('Sera que voce consegue adivinhar qual foi ?')

acertou = False
tentativa = 0

while not acertou:
    jogador = int(input('Qual e o seu palpite ? '))
    tentativa += 1
    if jogador == maquina:
        acertou = True
    else:
        if jogador < maquina:
            print('Mais... tente mais uma vez')
        elif jogador > maquina:
            print('Menos...tente mais uma vez')

print('Acertou com {} tentativas'.format(tentativa))
