#LOJA DE TINTAS

print("Qual tamanho da área a ser pintada")
area_ser_pintada = float(input()) # 100 m²

# 1 litro = 3 metros²
# 1 Lata = 18 litros = R$ 80,00
# 1 lata = 18*3 = 54 m²

metro_lata = 54

valor_lata = 80

quant_latas_necessrias = area_ser_pintada / metro_lata

valor_total_da_tinta = quant_latas_necessrias * valor_lata

print("Quantidade de Latas necessárias: ",round(quant_latas_necessrias))
print("Preço Total: ",valor_total_da_tinta)