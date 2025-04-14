frase = 'O Python é uma linguagem de programação ' \
        'multiparadigma. ' \
        'Python foi criado por Guido van Rossum.'

i = 0
count = 0

while i < len(frase):
    l = frase[i]

    if(frase.count(l) > count and l != ' '):
        letter = l
        count = frase.count(l)

    i += 1


print(f'A letra "{letter}" foi a que mais apareceu, contei {count} vezes')