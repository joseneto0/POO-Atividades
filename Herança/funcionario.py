class Funcionario:
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    def adicionaAumento(self, valor:float):
        self._salario += valor

    @property
    def ganhoAnual(self):
        return f"R$ {self._salario * 12:.2f}"
    
    @property
    def exibeDados(self):
        return f"Nome: {self._nome}, Salário: R$ {self._salario:.2f}"

class Assistente(Funcionario):
    def __init__(self, nome, salario, matricula):
        super().__init__(nome, salario)
        self._matricula = matricula

    @property
    def exibeDados(self):
        return f"Nome: {self._nome}, Salário: R$ {self._salario:.2f}, Matrícula: {self._matricula}"

class Tecnico(Assistente):
    def __init__(self, nome, salario, matricula, bonus=0):
        super().__init__(nome, salario, matricula)
        self._bonus = bonus

    @property
    def ganhoAnual(self):
        return f"R$ {(self._salario + self._bonus) * 12:.2f}"

    @property
    def exibeDados(self):
        return f"Nome: {self._nome}, Bônus: R$ {self._bonus:.2f}, Salário com Bônus: R$ {self._salario + self._bonus:.2f}, Matrícula: {self._matricula}"

class Administrativo(Assistente):
    def __init__(self, nome, salario, matricula, turno):
        super().__init__(nome, salario, matricula)
        turno = turno.lower()
        self._turno = turno
        
    @property
    def salario(self):
        if self._turno == 'noite':
            return self._salario + 500
        return self._salario

    @property
    def exibeDados(self):
        return f"Nome: {self._nome}, Turno: {self._turno.capitalize()}, Salário: R$ {self.salario:.2f}, Matrícula: {self._matricula}"