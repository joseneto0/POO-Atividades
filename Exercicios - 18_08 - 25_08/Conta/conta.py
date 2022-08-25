class ContaCorrente:
    def __init__(self, numero, saldo, nome):
        self.__numero = numero
        self.__saldo = saldo
        self.__nome = nome

    @property
    def numero(self):
        return self.__numero

    @property
    def nome(self):
        return self.__nome

    @property
    def saldo(self):
        return f"R$ {self.__saldo:.2f}"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor > self.__saldo:
            return False
        else:
            self.__saldo -= valor
            return True
