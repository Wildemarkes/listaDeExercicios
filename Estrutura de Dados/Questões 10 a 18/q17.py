# LOJA DE TINTAS

print("Qual tamanho da área a ser pintada")
area_ser_pintada = float(input())  # 100 m²

# 1 litro = 6 metros²
# 1 Lata = 18 litros = R$ 80,00
# 1 lata = 18*6 = 108 m²
# 1 galão = 3.6 litros = R$ 25,00
# 1 galão cobre 21,6 m²

metro_lata = 108
valor_lata = 80
metro_galao = 21.6
valor_galao = 25

if area_ser_pintada >= metro_lata:
    quant_latas_necessrias = area_ser_pintada / metro_lata
    valor_total_da_tinta = round(quant_latas_necessrias) * valor_lata
    print("Quantidade de Latas necessárias: ", quant_latas_necessrias)
    print("Preço Total: ", valor_total_da_tinta)
elif area_ser_pintada < metro_lata:
    quant_galao_necessario = round(area_ser_pintada / metro_galao)
    valor_total_da_tinta = quant_galao_necessario * valor_galao
    print("Quantidade de galões necessários: ", quant_galao_necessario)
    print("Preço Total: ", valor_total_da_tinta)



