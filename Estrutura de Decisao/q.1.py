# dias_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
# print("Informe o dia da Semana")
# dia = str(input())
# if dia == dias_da_semana[5] or dia == dias_da_semana[6]:
#     print("Hoje é dia de descanso")
# else:
#     print("Você precisa trabalhar")

# lista_frutas = ["Abacaxi", "Pêra", "Uva", "Maçã", "Morango"]
#
# for item in lista_frutas:
#     if item == "Morango":
#         print(item, "está na lista")

# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma
# lista

# tupla = (1, 2, 3, 4)
# lista = []
# for i in tupla:
#     double_i = i*2
#     lista.append(double_i)
# print(lista)

# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela

# for i in range(100,151,2):
#     print(i)

# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35,
# imprima as temperaturas na tela

# temperatura = 40
# while temperatura > 35:
#     print(temperatura)
#     temperatura = temperatura - 1
# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa

# contador = 0
# while contador < 100:
#     if contador == 23:
#         print("Número 23 encontrado")
#         break
#     else:
#         pass
#     print(contador)
#     contador = contador + 1

# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável
# for menor ou igual a 20, adicione à lista, apenas os valores pares e imprima a lista

# lista = []
# valor = 4
#
# while valor <= 20:
#     if valor % 2 == 0:
#         lista.append(valor)
#     valor = valor + 1
# print(lista)

# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na
# sua instrução de impressão


# frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."
#
# contador = 0
# for i in frase:
#     if i == "r":
#         contador = contador+1
# print(contador)


# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
# nums = range(5, 45, 2)
# lista = []
# for i in nums:
#     lista.append(i)
# print(lista)
import random
#
dezenas = list(range(1, 60))

# sorteados = random.sample(dezenas,6)
#
print(sorted(random.sample(dezenas, 6)))
#
#
# print(random.randrange(1, 25))
#
# loto_facil = [11, 22, 25, 19, 9, 4, 17, 10, 3, 23, 18, 1, 6, 8, 24]
#
# loto_facil.sort()
# print(loto_facil)
#
# print(sorted(loto_facil))
# print(len(loto_facil))


# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20
# (a função não recebe parâmetro) e depois faça uma chamada à função para listar os números


# def seq():
#     # numeros = list(range(1, 20))
#     lista = []
#     for i in range(1,21):
#         if i % 2 == 0:
#             lista.append(i)
#     print(lista)
#
# seq()


# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string
# em letras maiúsculas. Faça uma chamada à função, passando como parâmetro uma string

# def retornaMaiscula(nome):
#     return print(nome.upper())
#
# retornaMaiscula("wildemarkes")

# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e
# imprima a lista

# def func3(lista):
#     # lista = [item1, item2, item3, item4]
#     for i in lista:
#         return print(lista)
#
# elementos = [1, 2, 3, 4]
#
# elementos.append(6)
# elementos.append(7)
#
# func3(elementos)

# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos.
# Faça duas chamadas à função, com apenas 1 elemento e na segunda chamada com 4 elementos

# def func4(item, *vartuple):
#     print(item)
#
#     for i in vartuple:
#         print(i)
#
# func4("teste")
#
# func4("teste", 1, 2, 3, 4)

# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma.
# A expressão vai receber 2 números como parâmetro e retornar a soma deles

# soma = lambda num1, num2: num1+num2
#
# print(soma(num1=3,num2=4))


# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
from cgitb import reset

# Celsius = [39.2, 36.5, 37.3, 37.8]

# resultado = lambda fa: (Celsius * (9 / 5) + 32)
# for i in Celsius:
#     resultado = lambda fa: (i * (9 / 5)) + 32
#     # print(resultado(i))
#
#     Fahrenheit = map(resultado,Celsius)
#
#     print(list(Fahrenheit))

#
# Celsius = [39.2, 36.5, 37.3, 37.8]
#
# resultado = lambda Celsius: (Celsius * (9 / 5)) + 32
#
# Fahrenheit = map(resultado,Celsius)
#
# print(list(Fahrenheit))

# dict = {}
#
# print(dir(dict))


# ************* Desafio ************* (pesquise na documentação Python)

# Exercício 10 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo
# do arquivo. Dica, use Pandas e um de seus métodos, describe()
# Arquivo: "binary.csv"

# import pandas as pd
# import matplotlib.py
#
#
# file_name = "binary.csv"
#
# df = pd.read_csv(file_name)
#
# print(df.to_string())

