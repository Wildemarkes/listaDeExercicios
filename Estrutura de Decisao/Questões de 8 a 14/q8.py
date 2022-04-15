produtos = []

for i in range(1, 4):
    print("Cadastre o preço do",i,"º produto")
    produtos.append(float(input()))

print("este é o melhor preço: ", min(produtos))
