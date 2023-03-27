# 3 Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = 'id'
idade = -1
salario = -1
sexo = 'i'
estado = 'i'

while len(nome) < 3:
    nome = input("Digite seu nome: ")

while idade < 0 or idade > 150:
    idade = int(input("Digite sua idade: "))

while salario < 0:
    salario = float(input("Digite seu salário: "))

while sexo !='f' or sexo !='F' or sexo !='m' or sexo !='M':
    sexo = input("Digite F ou M para seu sexo: ")

while estado != 's' or estado != 'c' or estado != 'v' or estado != 'd':
    estado = input("Digite s para solteiro, c para casado, v para viúvo ou d para divorciado: ")