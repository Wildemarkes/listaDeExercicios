print(30 * "*", "Python Calculator", 30 * "*")

print("\nSeleciona o número para realizar uma operaçãon\n")

print("1 - Soma \n2 - Subtração\n3 - Multiplicação\n4 - Divisão")

opcao = int(input())

print("Digite primeiro número")
n1 = int(input())
print("Digite segundo número")
n2 = int(input())


if opcao == 1:
    soma = lambda n1, n2: n1 + n2
    print(soma(n1, n2))
elif opcao == 2:
    subtracao = lambda n1, n2: n1 - n2
    print(subtracao(n1, n2))
elif opcao == 3:
    multiplicacao = lambda n1, n2: n1 * n2
    print(multiplicacao(n1, n2))
elif opcao == 4:
    divisao = lambda n1, n2: n1 / n2
    if (n2 != 0):
        print(divisao(n1, n2))
    else:
        print("Impossível Dividir por zero")
else:
    print("Opção Inválida")

