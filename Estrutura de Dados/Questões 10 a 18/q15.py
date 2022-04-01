#considerando uma jornada de 8 horas diárias

print("Quanto você ganha por hora?")
valor_hora = float(input());

print("Quantas horas você trabalha por mês?")
total_horas = float(input());
salario = valor_hora * total_horas;

ir = 0.11
inss = 0.08
sindicato = 0.05

print("Salário Bruto: ", salario)
print("IR R$",salario*ir)
print("INSS R$",salario*inss)
print("Sindicato R$",salario*sindicato)
print("Salário Líquido R$",salario - ((salario*ir)+(salario*inss)+(salario*sindicato)))


