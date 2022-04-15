import math

#equação do segundo grau

a = int(input("informe o valor de A"))
b = int(input("informe o valor de B"))
c = int(input("informe o valor de C"))

delta = (b**2 - 4*a*c)

raiz = math.sqrt(delta)

x1 = (-b + raiz)/ (2 * a)
x2 = (-b - raiz )/ (2 * a)
#
print("\nValor de x1: {0:.2f}".format(x1))
print("\nValor de x1: {0:.2f}".format(x2))








