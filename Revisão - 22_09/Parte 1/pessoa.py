from datetime import datetime

class Pessoa:
    def __init__(self, nome: str, data: str, altura: float):
        self.nome = nome
        self.data = data
        self.altura = altura
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        assert type(nome) == str and nome.isalpha() == True, f"Digite um nome em string e sem digitos. Nome incorreto: {nome}"
        self.__nome = nome
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        meses_31 = [1, 3, 5, 7, 8, 10, 12]
        meses_30 = [4, 6, 9, 11]
        assert type(data) == str, f"Data tem que estar em string"
        if int(data[3:5]) in meses_31:
            assert len(data[:2]) == 2 and int(data[:2]) >= 1 and int(data[:2]) <= 31, f"Dia incorreto (Siga o modelo XX/XX/XXXX)"
        elif int(data[3:5]) in meses_30:
            assert len(data[:2]) == 2 and int(data[:2]) >= int('01') and int(data[:2]) <= int('30'), f"Dia incorreto (Siga o modelo XX/XX/XXXX)"
        else:
            assert len(data[:2]) == 2 and int(data[:2]) >= int('01') and int(data[:2]) <= int('28'), f"Dia incorreto (Siga o modelo XX/XX/XXXX)"
        assert data[2] == '/' and data[5] == '/', "Siga o Modelo XX/XX/XXXX para data, incluindo as '/'"
        assert len(data[3:5]) == 2 and int(data[3:5]) >= 1 and int(data[3:5]) <= 12, "Mês colocado inválido"
        assert (len(data[6:])) == 4, "Ano colocado inválido"
        self.__data = data
        
    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, altura):
        assert type(altura) == float, "Coloque a altura no tipo float"
        assert altura <= 3.5, "Não sabia que gigantes existiam :O" 
        self.__altura = altura
        
    def calcularIdade(self):
        dia, mes, ano = map(int, self.data.split('/'))
        anos = datetime.now().year - ano
        if datetime.now().month < mes:
            anos -= 1
        elif datetime.now().month == mes and datetime.now().day >= dia:
            anos += 1
        elif mes == datetime.now().month and dia > datetime.now().day:
            anos -= 1    
        assert anos >= 0, "Você colocou um ano que ainda não chegou :)"
        assert anos <= 200, "Você faz parte do eternos? Coloque o ano correto"
        return anos
    
    def imprimirDados(self):
        print(f"Olá, sou {self.nome}, tenho {self.calcularIdade()} anos e tenho {self.altura:.2f}m de altura")

if __name__ == '__main__':      
    try:   
        a = Pessoa('Jose', '16/06/2004', 1.75)
        print(a.nome)
        print(a.calcularIdade())
        a.imprimirDados()
    except AssertionError as erro:
        print(erro)