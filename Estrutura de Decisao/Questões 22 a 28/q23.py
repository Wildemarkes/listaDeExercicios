valor = float(input("Digite um número"))

# print(round(valor))

if valor == round(valor): #verifica se existe um número para arredondar
    print(f'{int(valor)} é um número inteiro')
else:
    print(f'{valor} é um número decimal')
