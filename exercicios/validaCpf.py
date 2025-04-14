cpf = list(input('Insira o CPF: '))

def valida_cpf(cpf):
    for digito in cpf:
        if digito == '.' or digito == '-':
            cpf.remove(digito)

    if len(cpf) != 11:
        return '\nCPF invalido'
    soma = 0
    contagem = 10
    for numero in cpf[:-2]:
        soma += (int(numero) * contagem)
        contagem -= 1

    digito_1 = (soma * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    if digito_1 == int(cpf[-2]):
        soma = 0
        contagem = 11
        for numero in cpf[:-1]:
            soma += (int(numero) * contagem)
            contagem -= 1

        digito_2 = soma % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        if digito_2 == int(cpf[-1]):
            return '\nValido'
        else:
            return '\nInvalido'
    else:
        return '\nInvalido'

print(valida_cpf(cpf))