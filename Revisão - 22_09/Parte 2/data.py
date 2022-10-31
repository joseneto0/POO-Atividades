class Data:
    def __init__(self, data : str):
        if type(data) == str and len(data[:2]) == 2 and data[2] == '/' and int(data[:2]) >= 1 and int(data[:2]) <= 31 and len(data[3:5]) == 2 and data[5] == '/' and int(data[3:5]) >= 1 and int(data[3:5]) <= 12 and len(data[6:]) == 4:
            self.data = data
        else:
            self.data = '01/01/0001'
        self.dia = self.data.split('/')[0]
        self.mes = self.data.split('/')[1]
        self.ano = self.data.split('/')[2]

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano
    
    def get_mes_extenso(self):
        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        return meses[int(self.mes) - 1]

    def compara(self, outra_data: object):
        if self.data == outra_data:
            return 0
        elif self.ano > outra_data.ano:
            return 1
        elif self.ano == outra_data.ano and self.mes > outra_data.mes:
            return 1
        elif self.ano == outra_data.ano and self.mes == outra_data.mes and self.dia > outra_data.dia:
            return 1
        else:
            return -1
    
    def is_bissexto(self):
        if int(self.ano) % 4 == 0 and int(self.ano) != 0 or int(self.ano) % 400 == 0:
            return True
        return False

    def clone(self):
        return Data(self.data)

    def __str__(self):
        return f"{self.dia} de {self.get_mes_extenso()} de {self.ano}"

if __name__ == '__main__':
    d1 = Data('05/11/2020')
    d2 = Data('22/09/2022')
    print(d1.dia)
    print(d1.mes)
    print(d1.ano)
    print(d1.get_mes_extenso())
    print(d1.compara(d2))
    print(d1.is_bissexto())
    print(d1)
    d3 = d1.clone()
    print(d3)