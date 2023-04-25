# 9 Faça um Programa que peça a temperatura em graus Farenheit, 
# transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).

temp = float(input('Qual a temperatura em graus Farenheit? '))
print(f'A temperatura é de {5 * (temp - 32) / 9:,.2f} graus Celsius.')