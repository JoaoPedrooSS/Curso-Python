from produtos import produtos
import copy

produtos_copiados = copy.deepcopy(produtos)

def aumentaPreco(produto):
        produto["preco"] += produto["preco"] * 0.10
        produto["preco"] = round(produto["preco"], 2)

if __name__ == "__main__":
    for produto in produtos_copiados:
        print(produto)
        aumentaPreco(produto)


    produtos_ordenados_por_nome = sorted(produtos_copiados, key=lambda produto: produto["nome"])
    print("\n---Produtos Ordenados por nome---\n")
    for produto in produtos_ordenados_por_nome:
        print(produto)

    produtos_ordenados_por_preco = sorted(produtos_copiados, key=lambda produto: produto["preco"])
    print("\n---Produtos Ordenados por preco---\n")
    for produto in produtos_ordenados_por_preco:
        print(produto)