import random
import time

adjetivo = ['Feroz','Macabro','Esperto','Bobão','Alto','Antigo','Belo','Curto','Agil','Pequeno']

substantivos = ['Tartaruga','Papagaio','Coelho','Lontra','Cachorro','Gato','Sapo','Macaco','Hiena','Urso']

print ('Bem - vindo Ao Gerador de Nomes aleatorios')

gerar = int (input ('Digite 1 Para Gerar um Nome ou 0 Para Encerrar: '))

if gerar == 1 :
    adjetivo = random.choice(adjetivo)
    substantivos = random.choice(substantivos)
    time.sleep(1)
    print ('{} {}'.format(substantivos,adjetivo))
elif gerar == 0:
    print('Encerrando...')
    time.sleep(1)
else:
    print ('Valor invalido.')