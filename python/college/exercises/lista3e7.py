maior = 0
menor = 0

for i in range (1, 6):
    num = float(input("Digite o %d número: " %i))
    
    if num > maior:
        maior = num
print("O maior número é %.2f" %maior)
