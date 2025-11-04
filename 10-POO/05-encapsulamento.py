class Conta:
    def __init__(self, n_agencia, saldo=0):
        self._saldo = saldo
        self.agencia = n_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

conta = Conta(1,100)
conta.depositar(100)
print(conta._saldo)