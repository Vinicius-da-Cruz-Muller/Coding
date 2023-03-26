# 10 Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitarM-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!"ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print("Digite seu turno!")
turno = input("Insira M, V ou N! ")

if turno == "m" or turno == "M":
    print("Bom dia!")
elif turno == 'v' or turno == "V":
    print("Boa tarde!")
elif turno == 'n' or turno == 'N':
    print("Boa noite!")
else:
    print("Valor inválido")