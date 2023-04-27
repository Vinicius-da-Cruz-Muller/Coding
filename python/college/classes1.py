class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def boas_vindas(self):
        print(f'Usuário: {self.nome}, Idade: {self.idade}')

usuario1 = Usuario(nome='Vinícius', idade='23')
usuario2 = Usuario(nome='Amarildo', idade='20')
usuario1.boas_vindas()
usuario2.boas_vindas()
print(usuario1.nome)
print(usuario2.idade)