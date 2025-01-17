import random 

palavras = ['casa','cavalo','macaco','carro','praia','castelo','historia','cama','macarrao']

def Jogar():
    escolha = random.choice(palavras)
    palavra_oculta = ['_'] * len(escolha)
    tentativas = 6
    letras_erradas = []

    print('Bem vindo ao Jogo da forca!')
    while tentativas > 0 and '_' in palavra_oculta:
        print(f'\nPalavra: {' '.join(palavra_oculta)}')
        print(f'\nTentativas: {tentativas}')
        print(f'\nLetras erradas:{", ".join(letras_erradas)}')
        
        palpite = input('\nDigite uma letra ou ? para tentar adivinhar a palavra: ').lower()
        if palpite == '?':
            chute = input('Qual a palavra ? ').lower()
            if chute == escolha:
                print('Parabens voce acertou')
                print(f'A palavra era {escolha}')
                break
            else:
                print('Voce errou')
                print(f'A palavra era {escolha}')
                break

        if palpite != 1 and not palpite.isalpha():
            print('\nPor favor, Digite uma letra.')
            continue
        if palpite in letras_erradas or palpite in palavra_oculta:
            print('Você já digitou essa letra.')
            continue  
        
        if palpite in escolha:
            print(f"\nBoa! A letra '{palpite}' está na palavra.")
            
            for i in range(len(escolha)):
                if escolha[i] == palpite:
                    palavra_oculta[i] = palpite
        else:
            print(f'\nLetra {palpite} nao esta na palavra')
            letras_erradas.append(palpite)
            tentativas -= 1
        
    
    if '_' not in palavra_oculta:
        print(f'\nA palavra era {escolha}')
        print('\nParabens voce venceu')
    elif tentativas == 0:
        print(f'A palavra era {escolha}')
        print('Voce perdeu!')
    
#Main

Jogar()