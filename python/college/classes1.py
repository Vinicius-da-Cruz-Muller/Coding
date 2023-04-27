class Usuario: #Palavra class diz ao interpretador que ali começa uma classe
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
usuario1.nome = 'Tywin'
print(usuario1.nome)


"""A palavra __init__ (com dois ‘_’ em cada lado) define o construtor, que terá
self como parâmetro (instância padrão), seguido dos parâmetros que
criarmos, separados por vírgula"""