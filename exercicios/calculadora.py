while True:
    try:
        numero_1 = int(input('Digite um número: '))
        op = input('Digite o operador (+, -, *, /, ^): ')
        numero_2 = int(input('Digite outro número: '))
    except:
        print('Entrada inválida!')
        continue

    if(op == '+'):
        res = numero_1 + numero_2
        print(res)
    elif(op == '-'):
        res = numero_1 - numero_2
        print(res)
    elif(op == '*'):
        res = numero_1 * numero_2
        print(res)
    elif(op == '/'):
        res = numero_1 / numero_2
        print(res)
    elif(op == '^'):
        res = numero_1 ** numero_2
        print(res)
    else:
        print('Operador invalido!')


    pergunta = input('Deseja sair? (s/n): ')
    if pergunta.lower() == 's':
        print('Saindo...')
        break
    elif pergunta.lower() == 'n':
        continue
    else:
        print('Resposta inválida!')
        print('Saindo...')
        break