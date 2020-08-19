#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

s = float(input('Digite o ganho por horas: '))
h = float(input('Digite a quantidade de horas trabalhadas: '))
salario_bruto = s * h 
IR = salario_bruto * 0.11
INSS = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (IR + INSS + sindicato)

print(f'Salario bruto: {salario_bruto}')
print(f'IR: {IR}')
print(f'INSS: {INSS}')
print(f'Sindicato {sindicato}')
print(f'Salario liquido {salario_liquido}')