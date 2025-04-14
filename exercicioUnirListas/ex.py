from itertools import zip_longest

def zipper (lista1, lista2):
    lista = min(len(lista1), len(lista2))

    return[
        (lista1[i], lista2[i]) for i in range(lista)
    ]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(l1, l2))

lista = zip_longest(l1, l2, fillvalue='Estado não informado')

print(list(lista))