
val = input("Entre com o valor: ")
valor_split = list(str(val))
valor_split

if len(valor_split)==2:
  print(valor_split[0]+' dezenas e '+valor_split[1]+' unidades')
elif len(valor_split)==1:
  print(valor_split[0]+' unidades')
elif len(valor_split)==3:
  print(valor_split[0]+' centenas,  '+ valor_split[1]+' dezenas e '+valor_split[2]+' unidades')
else:
  print("O valor tem mais que 9 centenas")