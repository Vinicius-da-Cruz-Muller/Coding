# 8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

horas = float(input('Quantas horas você trabalhou nesse mês?: '))
valor = float(input('Quanto você ganha por hora?:'))
print(f'Seu salário nesse mês será de R$ {horas * valor:,.2f} - valor bruto.')