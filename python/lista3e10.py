# 10 Faça um programa que receba dois números inteiros e 
# gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro, maior que o anterior: "))

for i in range(num1 + 1, num2):
    print(i, end = " ")