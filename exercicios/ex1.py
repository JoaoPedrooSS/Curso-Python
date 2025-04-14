nome = input('Digite seu nome: ')

if not nome:
    print('Desculpe, voce deixou os campos vazios.')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido: {nome[::-1]}')
    print(f'Seu nome{' ' not in nome and ' nao ' or ' '}contem espaços')
    print(f'Seu nome contem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra é {nome[len(nome) - 1]}')
