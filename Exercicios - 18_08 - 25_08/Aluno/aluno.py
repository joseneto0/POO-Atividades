from decimal import DivisionByZero
class Aluno:
    def __init__(self, matricula, nome):
        self.__matricula = matricula
        self.__nome = nome
        self.__notas = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def matricula(self):
        return self.__matricula % 100

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    def adicionar_notas(self, notas):
        self.__notas.append(notas)

    def media(self):
        try:
            result = sum(self.__notas) / len(self.__notas)
        except DivisionByZero:
            result = 0
        return f"Média: {result:.1f}"