from Conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, titular, identificador, saldo, senha, depositoInicial=0):
        super().__init__(titular, identificador, saldo, senha)
        self.saldo += depositoInicial