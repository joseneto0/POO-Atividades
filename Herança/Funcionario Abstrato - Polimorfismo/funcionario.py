from abc import ABC, abstractmethod
from enum import Enum
class GrauDeFormacao(Enum):
    ENSINO_MEDIO = 'Ensino Médio'
    ENSINO_SUPERIOR = 'Ensino Superior'
    ESPECIALISTA = 'Especialista'
    MESTRE = 'Mestre'
    DOUTOR = 'Doutor'

class Funcionario(ABC):
    def __init__(self, nome, salario, grau):
        self.nome = nome
        self.salario = salario
        self.grau = grau.value

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        assert type(nome) == str
        self.__nome = nome

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        assert type(salario) == float, f'Salário de {self.nome} fora do padrão Float (Tipo atual : {type(salario)})'
        self.__salario = salario

    @abstractmethod
    def contraCheque(self):
        return self.salario #+/* bonificacao

    @abstractmethod
    def addBonificação(self):
        pass
    
    def __str__(self):
        return f"Objeto do tipo {type(self).__name__}: {self.nome}, Salário: R$ {self.salario:.2f}"

class Presidente(Funcionario):
    def __init__(self, nome, salario, grau):
        super().__init__(nome, salario, grau)

    def addBonificação(self):
        if self.grau == 'Doutor':
            return 5
        return 3

    def contraCheque(self):
        return f'R$ {self.salario * self.addBonificação():.2f}'

class Gerente(Funcionario):
    def __init__(self, nome, salario, grau):
        super().__init__(nome, salario, grau)

    def addBonificação(self):
        if self.grau == 'Especialista':
            return 0.15 * self.salario
        elif self.grau == 'Mestre':
            return 0.25 * self.salario
        elif self.grau == 'Doutor':
            return 0.5 * self.salario

    def contraCheque(self):
        return f'R$ {super().contraCheque() + self.addBonificação():.2f}'

class Diretor(Gerente):
    def __init__(self, nome, salario, grau):
        super().__init__(nome, salario, grau)

    def addBonificação(self):
        return super().addBonificação() + 0.3 * self.salario

    def contraCheque(self):
        return super().contraCheque()