"""1.Classe Bola:
Crie uma classe que modele uma bola:
a.Atributos:cor, circunferência, material
b.Métodos: troca_cor e mostra_cor"""
class Bola:
    def __init__(self, cor, circunf, material):
        self.cor = cor
        self.circunf = circunf
        self.material = material

    def trocaCor(self):
        troca = input("Deseja mudar a cor atual ({})? [s/n]".format(self.cor))

        troca = troca[0].lower()

        if troca == "s":
            nova_cor = input("\n> Nova Cor: ")
            self.cor = nova_cor
        else:
            print("Ok, a cor continua {}".format(self.cor))

    def mostraCor(self):
        print("\nA cor atual é {}".format(self.cor))

def main():
    bola01 = Bola("azul", 5, "metal")

    while True:
        bola01.mostraCor()
        bola01.trocaCor()

        continuar = input("Continuar? [s/n]")
        continuar = continuar[0].lower()
        if continuar == "n":
            break

    bola01.mostraCor()
    

main()
