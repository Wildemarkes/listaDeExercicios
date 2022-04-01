# version 1.0
# print("Digite a primeira notar")
# n1 = float(input());
# print("Digite a segunda nota")
# n2 =float(input());
# print("Digite a terceira nota")
# n3 =float(input());
# print("Digite a quarta nota")
# n4 =float(input());
#
# media = (n1+n2+n3+n4)/4
#
# print("valor da media é: ", media)

# version 2.0 MELHORADO
notas = []
for contador in range(0, 4):  # aqui o range é exclusivo, neste caso, ele não inclui na contagem o 4 (0, 1, 2, 3)
    print("Digite a nota")
    notas.append(float(input()))  # método append() adiciona valores na lista
    if contador == 3:
        media = (notas[0] + notas[1] + notas[2] + notas[3]) / 4
        print("A média deste aluno é: ", media)
