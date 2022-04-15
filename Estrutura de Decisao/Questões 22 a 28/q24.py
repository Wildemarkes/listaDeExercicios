
listaNumeros = []

for i in range(0, 2):
    valor = float(input("Digite um valor"))
    listaNumeros.append(valor)

print("Qual operação deseja realizar "
      "\n 1 - Par ou Ímpar"
      "\n 2 - Positivo ou Negativo"
      "\n 3 - Inteiro ou Decimal")

opcao = int(input())


def parImpar(numero):
    if numero % 2 == 0:
        print(numero, " é: par")
    else:
        print(numero, "é ímpar")


def inteiroDecimal(valor):
    if valor == round(valor):  # verifica se existe um número para arredondar
        print(f'{int(valor)} é um número inteiro')
    else:
        print(f'{valor} é um número decimal')


def negativoPositivo(valor):
    if valor < 0:
        print(valor, "é negativo")
    else:
        print(valor, "É positovo")


if opcao == 1:
    for i in listaNumeros:
        parImpar(i)
elif opcao == 2:
    for i in listaNumeros:
        negativoPositivo(i)
elif opcao == 3:
    for i in listaNumeros:
        inteiroDecimal(i)
