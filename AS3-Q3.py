'''Escreva um programa que leia dois valores, um dividendo e um divisor.
Mostre o resultado da divisão e o resto da divisão inteira dos valores.'''

valor1 = int(input('Digite um Valor: '))
valor2 = int(input('Digite outro Valor: '))
print(f'''A divisão fica = {valor1 / valor2}
O resto da divisão = {valor1 % valor2}
E o resto da divisão inteira é = {valor1 // valor2}''')
