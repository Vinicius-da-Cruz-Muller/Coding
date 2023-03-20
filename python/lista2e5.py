# 5 Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:

print("Esse código calcula a média entre duas notas.")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2

if media == 10:
    print("Aprovado com distinção!")
elif media < 10 and media >= 7:
    print("Aprovado!")
else:
    print("Reprovado.")


