'''A Bate Ponto-LTDA bonifica seus funcionários de acordo o tempo de serviço
na empresa. Escreva um programa que leia o tempo de serviço do funcionário e
o valor do bônus por ano trabalhado. Mostre na tela quanto será a bonifficação
do funcionário.'''

tempo = int(input('Digite o tempo de serviço do funcionário:\n'))
valor = float(input('Digite o valor por ano:\nR$'))
print(f'''O tempo de Serviço do Funcionário foi de {tempo} ano(s)
e assim será gratificado com R${tempo * valor}''')
