#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

h = float(input('Digite sua altura: '))
print(f'Peso ideal masculino: {(72.7*h)-58}')
print(f'Peso ideal feminino: {(62.1*h)-44.7}')