#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso

print("Em que turno você estuda | digite M-matutino ou V-Vespertino ou N- Noturno.")

resposta = input()

#"Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
if resposta.upper() == "M":
    print("Bom Dia!")
if resposta.upper() == "V":
    print("Boa Tarde!")
if resposta.upper() == "N":
    print("Boa Noite!")
