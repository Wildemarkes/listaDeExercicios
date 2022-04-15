print("Escolha a sua opção de Carnes "
      "\n 1 - Filé Duplo"
      "\n 2 - Alcatra"
      "\n 3 - Picanha")
total = 0
opcao = int(input())
if opcao == 1:
    print("Uau Filé Duplo")
elif opcao == 2:
    print("Caracas Alcatra com molho é uma delícia")
elif opcao == 3:
    print("Você não é franco não hein!!!")

quantidade = int(input("Qual a quantidade de carnes meu padrão deseja"))


def forma_pagamento(total=None):
    print("Qual a forma de pagamento? 1 - Cartão, 2 - Dinheiro, 3 - Pix")
    fp = int(input())
    if fp == 1:
        print("Seu cartão é Tabajara Cliente? (S/N)")
        resposta = input()
        if resposta.upper() == "S":
            total = total - (total * 0.05)
            print(total)
        elif fp == 2 or 1:
            print("Essa forma de pagamento não possui desconto")
            print(total)


if opcao == 1:
    valor_carne_ate_5 = 4.9
    valor_carne_maior_5 = 5.8
    if quantidade <= 5:
        total = quantidade * valor_carne_ate_5
        print(total)
    else:
        total = quantidade * valor_carne_maior_5
        print(total)
    forma_pagamento(total)
elif opcao == 2:
    valor_file_ate_5 = 5.9
    valor_file_maior_5 = 6.8
    if quantidade <= 5:
        total = quantidade * valor_file_ate_5
    else:
        total = quantidade * valor_file_maior_5
    forma_pagamento(total)
elif opcao == 3:
    valor_picanha_ate_5 = 6.9
    valor_picanha_maior_6 = 7.8
    if quantidade <= 5:
        total = total * valor_picanha_ate_5
    else:
        total = total * valor_picanha_maior_6
    forma_pagamento(total)
