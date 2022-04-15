print("Interrogatório Policial")
print("Digite S - SIM, N - NÃO")
resposta = []

print("Telefonou para a vítima?")
resposta.append(input())
print("Esteve no local do crime?")
resposta.append(input())
print("Mora perto da vítima?")
resposta.append(input())
print("Devia para a vítima?")
resposta.append(input())
print("Já trabalhou com a vítima?")
resposta.append(input())

for i in range(len(resposta)):
    resposta[i] = resposta[i].upper()

if resposta.count('S') ==2:
    print("Suspeito")
elif resposta.count('S') == 3 or resposta.count('S') == 4:
    print('Cumplice')
elif resposta.count('S') == 5:
    print('Assasino')
else:
    print("Você é inocente")