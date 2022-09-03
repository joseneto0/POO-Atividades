class Ingresso:
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return f"R$ {self._valor:.2f}"

class IngressoVIP(Ingresso):
    def __init__(self, valor, adicional=0):
        super().__init__(valor)
        self.__adicional = adicional

    @property
    def valor(self):
        return f"R$ {self._valor + self.__adicional:.2f}"