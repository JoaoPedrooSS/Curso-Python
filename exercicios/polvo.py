import random

def escolhadoPolvo():
    return random.choice([1, 2])

print('Pergunte ao polvo')
op_1 = input('Opção 1: ')
op_2 = input('Opção 2: ')

opselecionada = escolhadoPolvo()

if(opselecionada == 1):
    print(f'O polvo disse {op_1}')
else:
    print(f'O polvo disse: {op_2}')