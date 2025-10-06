class Pessoa:
    # Constructor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade}')

pessoa_um = Pessoa('Eduarda', 18)
pessoa_um.apresentar()