# 3 Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letraescrever: F - Feminino, M - Masculino, Sexo Inválido.

s = str(input("Digite F ou M:"))

if s == 'F' or s == "f":
    print("Sexo feminino.")
elif s == 'M' or s == 'm':
    print("Sexo masculino.")
else:
    print("Sexo inválido.")
