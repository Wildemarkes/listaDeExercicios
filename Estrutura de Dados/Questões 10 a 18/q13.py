#calcular peso ideal a partir da fórmula (72.7*altura) - 58

print("Informe o seu sexo - M para Masculino ou F para Feminino")
sexo = input()
print("digite sua altura")
altura = float(input())

if sexo== "M":
    peso_ideal = (72.2 * altura) - 58
    print("O peso ideal para você é: ",peso_ideal)
elif sexo== "F":
    peso_ideal = (62.1 * altura) - 44.7
    print("O peso ideal para você é: ", peso_ideal)




