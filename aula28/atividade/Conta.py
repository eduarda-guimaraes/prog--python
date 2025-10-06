import random

class Conta:
    def __init__(self, titular, identificador, saldo, senha):
        self.titular = titular
        self.identificador = identificador
        self.saldo = saldo
        self.senha = senha
    
    def geraIdentificador(self):
        # gera um identificador aleatório com 5 números concatenados
        identificador = ""
        for i in range(5):
            aleatorio = random.randint(1, 1000)
            identificador += str(aleatorio)
        self.identificador = identificador

    def depositar(self, valor):
        self.saldo += valor

    def validaAcesso(self, identificador, senha):
        return self.identificador == identificador and self.senha == senha
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        return False
    
    def verificaSaldo(self):
        print(f"Seu saldo é de R${self.saldo:.2f}")
