'''Escreva um programa que leia o preço de um produto e mostre na tela o valor
com 10% de desconto arredondado para duas casas decimais.'''

preço = float(input('Digite o Preço do Produto:\nR$'))
print(f'O Valor do Produto ficou por R${preço - (preço * 10 / 100):.2f}')


