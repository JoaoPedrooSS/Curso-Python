quiz = [
    {
    'pergunta': 'Quanto é 2+2?',
    'opcoes': ['1', '5', '6', '4'],
    'resposta': '4'
    },
     {
    'pergunta': 'Quanto é 5*5?',
    'opcoes': ['25', '55', '45', '15'],
    'resposta': '25'
    },
    {
    'pergunta': 'Quanto é 1/2?',
    'opcoes': ['1,5', '0,5', '0,25', '1'],
    'resposta': '0,5'
    }
]
acertos = 0
for quest in quiz:
    print(quest.get('pergunta'))
    for indice, op in enumerate(quest.get('opcoes')):
        print(f'{indice}) {op}')
    while True:
        try:
            resp = input('Escolha uma opção: ')
            respCorreta = quest['opcoes'][int(resp)]
            break
        except ValueError:
            print('\nEntrada inválida!\n')
        except IndexError:
            print('\nEntrada invalida\n')

    if respCorreta == quest.get('resposta'):
        print('\nAcertou!!\n')
        acertos += 1
    else:
        print('\nErrou...\n')

print(f'Parabéns! voce acertou {acertos} de {len(quiz)}')