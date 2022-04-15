#João Bom de Papo

print("Informe a quantidade de peixe pescado")
peixe_pescado = float(input())
permitido = 50
if peixe_pescado>permitido:
    excesso = peixe_pescado-permitido
    multa = excesso*4
    print("Você pescou",peixe_pescado,"kg de peixes")
    print("Você pescou",excesso,"kg além do permitido")
    print("Você passou do limite permitido, sua multa é de: R$",multa,"reais")
else:
    print("Você pescou: ",peixe_pescado,"kg de peixes")

