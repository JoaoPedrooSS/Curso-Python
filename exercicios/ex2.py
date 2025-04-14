nome = input('Digite seu nome: ')
novoNome = '*'
contador = 0

while contador < len(nome):
    novoNome += nome[contador]
    novoNome += '*'
    contador += 1

print(novoNome)