# 8 Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
for i in range (1, 6):
    num = float(input("Digite o %d número: " %i))
    
    soma += num
print("A média dos números é %.2f" %(soma/5))