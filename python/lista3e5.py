# 5 Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
# Valide a entrada e permita repetir a operação.

popa = float(input("Digite o tamanho da população A: "))
t1 = float(input("Digite a taxa de crescimento da população A: "))
popb = float(input("Digite o tamanho da população B: "))
t2 = float(input("Digite a taxa de crescimento da população B: "))
ano = 0

while popa <= popb:
	popa += popa * (t1/100)
	popb += popb * (t2/100)
	ano += 1

print ( "A população A ultrapassa ou iguala a população B em %d anos" %ano )