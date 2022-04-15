notas = []

for i in range(0, 2):
    notas.append(float(input("digite uma nota")))

media = sum(notas) / 2

if media == 10:
    print("Aprovado com distinção")
if 7 <= media < 10:
    print("Aprovado")
if media < 7:
    print("Reprovado")
