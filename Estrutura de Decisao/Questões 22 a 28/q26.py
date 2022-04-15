print("Qual tipode combustível - A-álcool, G-gasolina")
tipo = input().upper()

quantidade_litros = int(input("Informe a quantidade"))

preco_gasolina = 2.5
preco_alcool = 1.9


def descontoAlcool():
    if quantidade_litros <= 20:
        total = preco_alcool * quantidade_litros
        total = total - (total*0.03)
        print("total a ser pago: ",total)
    elif quantidade_litros > 20:
        total = preco_alcool * quantidade_litros
        total = total - (total * 0.05)
        print("total a ser pago: ", total)
def descontoGasolina():
    if quantidade_litros <= 20:
        total = preco_gasolina * quantidade_litros
        total = total - (total * 0.04)
        print("total a ser pago: ", total)
    elif quantidade_litros > 20:
        total = preco_gasolina * quantidade_litros
        total = total - (total * 0.06)
        print("total a ser pago: ", total)

if tipo == 'A':
      descontoAlcool()
elif tipo == "G":
      descontoGasolina()