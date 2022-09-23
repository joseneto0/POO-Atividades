from data import Data
class Aviao:
    def __init__(self, numero_voo, data:object, horario):
        self.numero_voo = numero_voo
        self.data = data
        self.horario = horario
        self.__cadeiras = []

    @property
    def numero_voo(self):
        return self.__numero_voo

    @numero_voo.setter
    def numero_voo(self, numero_voo):
        self.__numero_voo = numero_voo

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario):
        assert type(horario) == str and horario[2] == ':' and len(horario[:2]) == 2 and len(horario[3:]) == 2, "Horário Inválido (siga o padrão XX:XX)"
        self.__horario = horario

    def vagasDisponiveis(self):
        return f'{100 - len(self.__cadeiras)} cadeiras disponíveis'

    def estaDisponivel(self, num_cadeira):
        assert num_cadeira not in self.__cadeiras, f"Cadeira {num_cadeira} indisponível"
        return f'Cadeira {num_cadeira} está disponível'

    def ocupar(self, num_cadeira):
        assert num_cadeira not in self.__cadeiras and len(self.__cadeiras) < 100, f"Cadeira {num_cadeira} indisponível"
        assert num_cadeira > 0 and num_cadeira < 101, f"Assento {num_cadeira} não existente"
        self.__cadeiras.append(num_cadeira)
        return f'Cadeira {num_cadeira} alocada com sucesso'

    def getAssento(self):
        assert len(self.__cadeiras) < 100, "Avião Cheio"
        assentos_disponiveis = [x for x in range(1, 101) if x not in self.__cadeiras]
        return f"Assentos Disponíveis: {assentos_disponiveis}"

    def clone(self):
        return Aviao(self.numero_voo, self.data, self.horario)

if __name__ == '__main__':
    try:
        d = Data('10/06/2001')
        aviao1 = Aviao(12314, d, '18:35')
        print(aviao1.numero_voo)
        print(aviao1.data)
        print(aviao1.horario)
        print(aviao1.getAssento())
        print(aviao1.ocupar(1))
        print(aviao1.ocupar(100))
        print(aviao1.vagasDisponiveis())
        a = aviao1.clone()
        print(a.data)
    except AssertionError as a:
        print(a)