list_shopping = []
while True:
    resp = input("\nInserir (I) Apagar (A) Listar (L) Sair (S): ").lower()

    if resp == 'i':
        item = input('Item: ')
        list_shopping.append(item)

    elif resp == 'a':
        if len(list_shopping) == 0:
            print('A lista esta vazia')
            continue

        try:
            index = int(input('Indice: '))
            del list_shopping[index]
        except IndexError:
            print('Esse indice não existe na lista!')
            continue
        except ValueError:
            print('Indice invalido!')
            continue

    elif resp == 'l':

        if len(list_shopping) == 0:
            print('A lista esta vazia')
        else:
            for index, item in enumerate(list_shopping):
                print(index, item)

    elif resp == 's':
        print('Saindo...')
        break
    else:
        print('Resposta invalida!\n')
        continue
