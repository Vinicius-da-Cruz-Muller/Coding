# 2 Faça um programa que leia um nome de usuário e a sua senha e 
# não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.
user = 'default'
senha = 'default'

while user == senha:
    print("O nome de usuário e a senha não podem ser iguais!")
    user = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")
print("Operação finalizada com sucesso!")

