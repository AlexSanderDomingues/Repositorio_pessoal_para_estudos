Livro = dict()
biblioteca = list()

def cadastrar():
    Livro['Titulo'] = input('Qual o Titulo do Livro ? ')
    Livro['Status'] = input('Qual o Status do Livro ? ')
    Livro['Genero'] = input('qual o Genero do Livro ? ')
    Livro['Autor'] = input('Qual o Autor do Livro ? ')
    Livro['Nota'] = float(input('Qual A nota do seu Livro ? '))
    biblioteca.append(Livro.copy())

def mostrar_Livros():
    for livro in biblioteca:
        print(f'Titulo: {livro['Titulo']}| Status: {livro['Status']}| Genero: {livro['Genero']}| Autor: {livro['Autor']}| Nota: {livro['Nota']}')   
        print()






# Main

while True:
    cadastrar()
    continuar = input('Deseja continuar ? S/N ').upper()[0]
    
    if continuar not in 'SN':
        print('Opçao Invalida. Tente novamente...')
    elif continuar =='N':
        break

mostrar_Livros()
    