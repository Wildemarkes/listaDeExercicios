nota1 = float(input("Digite a primeira nota"))
nota2 = float(input("Digite a segunda nota"))

media = (nota1+nota2)/2

if media >=9:
    print("A")
elif media < 9 and media >= 7.5:
    print("B")
elif 7.5 > media >= 6:
    print("C")
elif 6 > media >= 4:
    print("D")
elif media < 4:
    print("E")
