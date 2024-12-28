resposta = 'SIM'

while resposta == 'SIM':
    numero_1 = int(input(''))
    operacao = input('')
    numero_2 = int(input(''))
    if operacao == '+':
        soma = numero_1 + numero_2
        print('{} {} {} = {}'.format(numero_1, operacao, numero_2, soma))
    elif operacao == '-':
        subtracao = numero_1 - numero_2
        print('{} {} {} = {}'.format(numero_1, operacao, numero_2, subtracao))
    elif operacao == '/':
        if numero_2 != 0:
            escolha = input('Divisão inteira? ').upper()
            if escolha == 'SIM':
                divisao = numero_1 // numero_2
                print('{} {} {} = {}'.format(numero_1, operacao, numero_2, divisao))
            elif escolha == 'NAO':    
                divisao = numero_1 / numero_2
                print('{} {} {} = {}'.format(numero_1, operacao, numero_2, divisao))
        else:
            print('Divisão por zero')
    elif operacao == 'x':
        multiplicacao = numero_1 * numero_2
        print('{} {} {} = {}'.format(numero_1, operacao, numero_2, multiplicacao))
    elif operacao == '**':
        potencia = numero_1 ** numero_2
        print('{} {} {} = {}'.format(numero_1, operacao, numero_2, potencia))
    elif operacao == '%':
        porcentagem = numero_1 * (numero_2 / 100)
        print('{} {} {} = {}'.format(numero_1, operacao, numero_2, porcentagem))
    else:
        print('Inválido')

    resposta = input('Deseja continuar? ').upper()
