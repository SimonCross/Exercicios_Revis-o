# exercicios de fixação

# 1 - Escreva um programa que use um loop while para imprimir os números pares de 0 a 10.

'''
contador= 0

while contador <= 10:
    print(f"Contador: {contador}")
    contador +=2
'''

'''
# 2 - Crie uma lista com números inteiros e remova todos os números ímpares.
# Em seguida, imprima a lista resultante

lista =[1,2,3,4,5,6,7,8,9,10]

print(f"Lista inicial : {lista}")

# Adicionando elementos na lista

lista.append(11)
lista.append(12)

print(f"Lista de numeros com adição de novos numeros: {lista}")

# O comando Abaixo serve para modificar coisa NA LISTA
lista[0] = 0

lista.remove(3)
lista.remove(5)
lista.remove(7)
lista.remove(9)
lista.remove(11)

print(f"Esta a lista atual com os numeros impares retirados: {lista}")
'''

# 3 - Crie uma função que recebe um número como parâmetro e
# retorna True se o número for positivo e False se for negativo.

'''
par = int(input(f"coloque um numero inteiro: "))
confirmar = input(f"O numero selecionado foi {par} confima a solicitação?: ")

num = True

if par > 0:

    print(f"O numero que foi selecionado é positivo sendo ele é {par} de retorno {num}")
elif par < 0:
    num = False
    print(f"O numero que foi selecionado é negativo sendo ele é {par} de retorno {num}")

else:
    print("ok")
'''
