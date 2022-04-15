
valorHora = float(input("Informe o valor da hora trabalhada"))
quantHoras = int(input("Informe a quantidade de horas"))
salBruto = valorHora * quantHoras

def calculoDescontos(ir):

    inss = salBruto * 0.1
    sindicato = salBruto * 0.3
    fgts = salBruto * 0.11
    descontos = ir + inss + sindicato
    salLiquido = salBruto - descontos
    print("Salário Bruto: ",salBruto)
    print("Imposto de Renda: ",ir)
    print("INSS: ",inss)
    print("FGTS: ",fgts)
    print("Total de descontos: ",descontos)
    print("Salário Líquido: ",salLiquido)

if salBruto <=900:
    print("Isento")
elif salBruto <= 1500:
    ir = salBruto * 0.05
    calculoDescontos(ir)
elif salBruto <=2500:
    ir = salBruto * 0.1
    calculoDescontos(ir)
elif salBruto >2500:
    ir = salBruto * 0.2
    calculoDescontos(ir)


