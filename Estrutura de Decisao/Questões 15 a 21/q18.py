#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

def data_valida(valor_data):
    # separa a lista e atribui os valores para cada variável correspondente
    dia, mes, ano = map(int, data.split("/"))

    #verifica a validade do ano e do mês
    if mes < 1 or mes > 12 or ano <=0:
        print("Mês ou Ano inválido")

    #verifica qual mês tem 31
    if mes in (1,3,5,8,10,12):
        ultimo_dia = 31

    elif mes == 2:
        # verifica se o ano é bissexto
        if ano % 4 == 0 and ano % 400 == 0 or ano % 100 != 0:
            ultimo_dia = 29
        else:
            ultimo_dia = 28
    else:
        ultimo_dia = 30

    #verifica se o dia informado na data é válido
    if dia < 1 or dia > ultimo_dia:
       print("data inválida")
    else:
       print("data válida")

data = input("informe uma data no formato dd/mm/aaaa\n")

data_valida(data)




