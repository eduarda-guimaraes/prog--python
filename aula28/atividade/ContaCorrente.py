from Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, titular, senha, limite):
        super().__init__(titular, None, 0, senha)  
        self.limite = limite
        self.saldo = 0
    
    def sacar(self, valor):
        if self.saldo+self.limite>=valor:
            self.saldo-=valor
            return True
        return False
    
    def verificaSaldo(self):
        info = f"Seu saldo é de R${self.saldo}"
        if self.saldo < 0:
            info+=f"Limite disponível: R${self.saldo + self.limite}"
        else:
            info+=f"Limite disponível: R${self.limite}"
        return info