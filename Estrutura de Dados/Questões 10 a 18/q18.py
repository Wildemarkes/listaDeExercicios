#calcular vecolidade de download

print("Qual tamanho do arquivo para download?")
tamanho= float(input())

print("Qual velocidade de download")
velocidade = float(input())

tempo_download = tamanho /(velocidade/8)

print(tempo_download)