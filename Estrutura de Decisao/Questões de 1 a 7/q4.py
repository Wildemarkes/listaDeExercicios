vogais = ["A", "E", "I", "O", "U"]
consoates = ["B","C","D","E","F","G","H","I","J","L","M","N","P","Q","R","S","T","W","X","Y","Z",]

letra = input("Digite uma letra do alfabeto")

if letra.upper() in vogais:
    print("A letra digitada é uma vogal")
elif letra.upper() in consoates:
    print("a letra digitada é uma consoante")