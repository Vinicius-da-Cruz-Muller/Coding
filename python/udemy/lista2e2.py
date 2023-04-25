# 2 Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = float(input("Digite um número positivo ou negativo: "))
if num < 0:
    print("Número negativo.")
elif num == 0:
    print("Número zero.")
else:
    print("Número positivo.")