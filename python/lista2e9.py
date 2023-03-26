# 9 Faça um Programa que leia três números e mostre-os em ordem decrescente.
print("Esse código pede três números e os mostra em ordem decrescente.")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print("Os números na ordem decrescente: ", n1, n2, n3)
    else:
        print("Os números na ordem decrescente: ", n1, n3, n2)
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print("Os números na ordem decrescente: ", n2, n1, n3)
    else:
        print("Os números na ordem decrescente: ", n2, n3, n1)
elif n3 > n1 and n3 > n2:
    if n1 > n2:
        print("Os números na ordem decrescente: ", n3, n1, n2)
    else:
        print("Os números na ordem decrescente: ", n3, n2, n1)
else:
    print("Erro inesperado.")

