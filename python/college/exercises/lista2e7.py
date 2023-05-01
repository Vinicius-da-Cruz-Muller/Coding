# 7 Faça um Programa que leia três números e mostre o maior e o menor deles.
print("Esse código mostra o maior e o menor entre três números.")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print(f"O número {n1} é o maior número")
elif n2 > n1 and n2 > n3:
    print(f"O número {n2} é o maior número.")
else:
    print(f"O número {n3} é o maior número.")

if n1 < n2 and n1 < n3:
    print(f"O número {n1} é o menor número")
elif n2 < n1 and n2 < n3:
    print(f"O número {n2} é o menor número.")
else:
    print(f"O número {n3} é o menor número.")