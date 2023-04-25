'''
Interpolação de strings
s - string
d e i - int
f - float
x e X - hexadecimal

'''
nome = 'Vinícius'
preco = 1000.958976
variavel = "%s, o preço é de R$%.2f" % (nome, preco)
print(variavel)
print("O hexadecimal de %.1f é %x ou %04x" % (1500, 1500, 1500))