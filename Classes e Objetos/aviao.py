class Aviao:
    def __init__(self, numero_voo, data, horario):
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
        assert type(data) == str and data[2] == '/' and data[5] == '/' and len(data[:2]) == 2 and len(data[3:5]) == 2 and len(data[6:]) == 4, "Data Inválida (siga o padrão: XX/XX/XXXX)"
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
        if num_cadeira not in self.__cadeiras:
            return f'Cadeira {num_cadeira} está disponível'
        return f'Cadeira {num_cadeira} indisponível'

    def ocupar(self, num_cadeira):
        assert num_cadeira not in self.__cadeiras and len(self.__cadeiras) < 100, f"Cadeira {num_cadeira} indisponível"
        self.__cadeiras.append(num_cadeira)
        return f'Cadeira {num_cadeira} alocada com sucesso'

    @property
    def getAssento(self):
        assert len(self.__cadeiras) < 100 and len(self.__cadeiras) > 0, "Avião Cheio"
        assentos_disponiveis = [x for x in range(1, 100) if x not in self.__cadeiras]
        return f"Assentos Disponíveis: {assentos_disponiveis}"

    def __str__(self):
        return f'Bem Vindo ao Voo {self.numero_voo}.\nNo momento, temos {100-len(self.__cadeiras)} assentos disponíveis.\nTenha um bom voo :)'