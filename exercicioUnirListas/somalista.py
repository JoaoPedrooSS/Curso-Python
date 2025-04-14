l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [1, 2, 3, 4, 5, 6]

def soma_lista(lista1, lista2):
    return [lista1[i] + lista2[i] for i in range(min(len(lista1), len(lista2)))]
print(soma_lista(l1, l2))