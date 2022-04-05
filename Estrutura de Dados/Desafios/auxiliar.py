print("Quantos Cartões deseja utilizar?")

opcao = int(input())

card4 = []
card5 = []
card6 = []
card7 = []


def escolher_cartao():
    if opcao == 4:
        print("Pense em um número entre 1..15")
        op_4 = list(range(1, 17, 2))
        for item in op_4:
            card4.append(item)
    if opcao == 5:
        print("Pense em um número entre 1..31")
        op_5 = list(range(1, 32, 2))
        for item in op_5:
            card5.append(item)
    if opcao == 6:
        print("Pense em um número entre 1..63")
        op_6 = list(range(1, 64, 2))
        for item in op_6:
            card6.append(item)
    if opcao == 7:
        print("Pense em um número entre 1..128")
        op_7 = list(range(1, 128, 2))
        for item in op_7:
            card7.append(item)



def print_ask(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Olá, {name}')  # Press Ctrl+8 to toggle the breakpoint.

def advinhar():
    resultado = 0

    r1 = input(f'O numero está aqui? (S/N) -> {card4}')
    if r1.upper() == "S":
        resultado = resultado + 1

    r2 = input(f'O numero está aqui? (S/N) -> {card5}')
    if r2.upper() == "S":
        resultado = resultado + 2

    r3 = input(f'O numero está aqui? (S/N) -> {card6}')
    if r3.upper() == "S":
        resultado = resultado + 4

    r4 = input(f'O numero está aqui? (S/N) -> {card7}')
    if r4.upper() == "S":
        resultado = resultado + 8

    print(f'Você pensou no número: {resultado}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    escolher_cartao()

    ja_pensou = input('E ai, já pensou? (S/N) ')

    if ja_pensou.upper() != "S":
        print('Pois ande logo!')
    else:
        print('Não vai esquecer o número...')

    advinhar()

    correto = input(f'Acertei? (S/N)')
    if correto.upper() == "S":
        print('Eu sou demais!!! ;-)')