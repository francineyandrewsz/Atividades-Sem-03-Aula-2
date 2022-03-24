'''Escreva um program que leia o valor de um raio, calcule e mostre na tela
o comprimento da circunferência, a área do círculo, a área da esfera e o
volume da esfera para o valor do raio lido. Mostre os valores com 6 casa decimais.'''

raio = float(input('Digite o raio:\n'))
Pi = 3.141592
circunferencia = 2 * Pi * raio
area_circulo = Pi * raio ** 2
area_esfera = 4 * Pi * raio
volume_esfera = 4 / 3 * Pi * raio ** 3
print(f'O valor da Circunferência = {circunferencia:.6f}')
print(f'O valor da Área do Círculo = {area_circulo:.6f}')
print(f'O valor da Área da Esfera = {area_esfera:.6f}')
print(f'O valor do Volume da Esfera = {volume_esfera:.6f}')
