def mult(*args):
    res = 1
    for arg in args:
        res *= arg
    return res

def par(x):
    if x % 2 == 0:
        return 'Par'
    else:
        return 'impar'

#função que cria função
def cria_mult(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = cria_mult(2)
triplica = cria_mult(3)
quadruplica = cria_mult(4)

print(duplica(2))
print(triplica(2))
print(quadruplica(2))