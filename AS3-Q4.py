'''Escreva um programa que leia uma quantidade de minutos e mostre a
quantidade de horas e minutos equivalente.'''

q_min = int(input('Digite a quantidade de minutos:\n'))
h = q_min // 60
m = q_min % 60
print(f'{q_min} equivale a {h} hora(s) e {m} minuto(s).')

