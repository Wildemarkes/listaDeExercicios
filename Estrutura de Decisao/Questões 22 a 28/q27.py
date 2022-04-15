print("1 - Morango - R$ 2,5 até 5 kg ou Acima por R$ 2,20")
quanMorango = int(input("Quantos kilos de Morango deseja comprar"))

print("2 - Maçã - R$ 1,8 até 5 kg ou Acima por R$ 1,5")
quanMaca = int(input("Quantos kilos de Maçã deseja comprar"))

preco_morango_1 = 2.5
preco_morango_2 = 2.2

preco_maca_1 = 2.5
preco_maca_2 = 2.2


def descontoGeral(total):
    if quanMorango + quanMaca >= 8 or total > 25:
        total = total - (total * 0.1)
        print("Você conseguiu um desconto de 10%: ", total)


def descontoMaca():
    if quanMaca <= 5:
        total = preco_maca_1 * quanMaca
        descontoGeral(total)
        print("total a ser pago: ", total)
    elif quanMaca > 5:
        total = preco_maca_2 * quanMaca
        descontoGeral(total)
        print("total a ser pago: ", total)



def descontoMorango():
    if quanMorango <= 5:
        total = preco_morango_1 * quanMorango
        print("total a ser pago: ", total)
        descontoGeral(total)
    elif quanMorango > 5:
        total = preco_morango_2 * quanMorango
        descontoGeral(total)
        print("total a ser pago: ", total)


descontoMaca()
descontoMorango()
