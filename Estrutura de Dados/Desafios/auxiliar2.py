from tkinter import *


class Application:  # inicia a aplicação
    def __init__(self, master=None):
        self.text_pense = None
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Programa Advinho")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.num_cards = Label(self.segundoContainer, text="Insira o número de cartões", font=self.fontePadrao)
        self.num_cards.pack(side=LEFT)

        self.inp_num_cards = Entry(self.segundoContainer)
        self.inp_num_cards["width"] = 30
        self.inp_num_cards["font"] = self.fontePadrao
        self.inp_num_cards.pack(side=LEFT)

        self.gen = Button(self.quartoContainer)
        self.gen["text"] = "Gerar"
        self.gen["font"] = ("Calibri", "8")
        self.gen["width"] = 12
        self.gen["command"] = self.gerarCards
        self.gen.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def binvet(self, n_max):  # Cria uma lista de Binários
        a = []
        for i in range(0, n_max):
            a.append("{0:b}".format(i + 1))

        return a

    def cardsgen(self, num, b):  # função geradora de cartões
        cards = []  # cria matriz cartão
        for i in range(num):
            cards.append([])

        for i in range(len(b)):  # interar sobre a lista dos binários
            binarioat = b[len(b) - i - 1]  # binário atual decrescente
            n_card = len(binarioat)  # tamanho do binário
            for a in binarioat:  # interar sobre cada elemento binário
                if a == '1':  # verificar se o número pertence a tal posição
                    cards[n_card - 1].append(len(b) - i)  # adiciona o número a tal cartão
                n_card = n_card - 1

        return cards

    def gerarCards(self):

        n_cartoes = self.inp_num_cards.get()
        n_cartoes = int(n_cartoes)

        n_max = 2 ** n_cartoes - 1  # Verifica o número maximo possivel

        self.text_pense = Label(self.terceiroContainer, text="Agora pense em um número de 1 a {n_max}",
                                font=self.fontePadrao)
        self.text_pense.pack(side=LEFT)

        vetorBinarios = self.binvet(n_max)  # retorna lista de número em binário
        cartoes = self.cardsgen(n_cartoes, vetorBinarios)  # Retorna os Cartões

        print("Agora pense em um número de 1 a ", n_max)
        ja_pensou = input('E ai, já pensou? (S/N) ')

        if ja_pensou.upper() != "S":
            print('Pois ande logo!')
        else:
            print('Não vai esquecer o número...')

        a = 0
        for i in range(len(cartoes)):
            b = str(cartoes[i])
            R = input("Seu número está aqui/n? s\n" + b)
            if R == 's':
                a = a + 2 ** i
        print("Seu número é", a)

        correto = input(f'Acertei? (S/N)')
        if correto.upper() == "S":
            print('Eu sou demais!!! ;-)')


root = Tk()
Application(root)
root.mainloop()
