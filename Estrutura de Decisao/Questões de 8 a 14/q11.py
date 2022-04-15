salario = float(input("Informe seu salário"))


def informacoes(taxa):
    totalAumento = salario*taxa
    novoSalario = salario + totalAumento
    valorTaxa = taxa*100;
    print("Salário antes do reajuste",salario)
    print("Ajuste do salário: {:.2%}".format(taxa))
    print("Valor do aumento: ",totalAumento)
    print("Novo Salário",novoSalario)

if salario <=280:
    # salario = salario + (salario * 0.2)
    # print("Salário Atual",salario)
    informacoes(0.2)
elif salario <= 700 or salario >= 281:
    # salario = salario + (salario * 0.15)
    # print("Salário Atual", salario)
    informacoes(0.15)
elif salario >= 1500 or salario <= 701:
    # salario = salario + (salario * 0.1)
    # print("Salário Atual", salario)
    informacoes(0.1)
elif salario >1500:
    # salario = salario + (salario * 0.05)
    # print("Salário Atual", salario)
    informacoes(0.05)


