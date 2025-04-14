def adicionar(x):
    def interna(y):
        return x + y  # "x" já está definido, "y" será fornecido depois
    return interna  # Retorna a função sem executar

soma_com_dez = adicionar(10)  # Cria uma função que soma 10
print("programa rodando")


print(soma_com_dez(5))  # Saída: 15
