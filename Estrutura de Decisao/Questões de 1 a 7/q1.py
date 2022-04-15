
numero1 = int(input("Digite primeiro valor"))

print("Digite segundo valor")
numero2 = int(input())

if numero1 > numero2:
    print(numero1, "é maior que ",numero2)
elif numero2 > numero1:
    print(numero2, "é maior que ",numero1)
else:
    print("os números são iguais")