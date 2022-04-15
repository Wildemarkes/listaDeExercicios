ladoA = input("Digite o lado A")
ladoB = input("Digite o lado B")
ladoC = input("Digite o lado C")
#
# if ladoA+ladoB > ladoC or ladoA+ladoC > ladoB or ladoB+ladoC > ladoA:
#     print("É um triângulo")
if ladoA==ladoB and ladoA==ladoC and ladoC==ladoB:
    print("Triângulo Equilátero")
elif ladoA==ladoB or ladoB==ladoC or ladoA==ladoC:
    print("Triângulo isóscelos")
elif ladoA != ladoB and ladoA != ladoC and ladoB != ladoC:
    print("Triângulo Escaleno")