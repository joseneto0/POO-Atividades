class País:
    def __init__(self, nome, nome_capital, dimensao):
        self.__nome = nome
        self.__nome_capital = nome_capital
        self.__dimensao = dimensao
        self.__paises_fronteira = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def nome_capital(self):
        return self.__nome_capital
    
    @nome_capital.setter
    def nome_capital(self, nome_capital):
        self.__nome_capital = nome_capital

    @property
    def dimensao(self):
        return self.__dimensao
    
    @dimensao.setter
    def dimensao(self, dimensao):
        self.__dimensao = dimensao

    @property
    def paises_fronteira(self):
        return self.__paises_fronteira
    
    def adicionar_paises_fronteira(self, pais):
        if pais not in self.__paises_fronteira:
            self.__paises_fronteira.append(pais)
        else:
            return "Já está registrado :D"

    def __str__(self):
        return f"País: {self.__nome}\nCapital: {self.__nome_capital}\nDimensão: {self.__dimensao} km\nPaíses cadastrados que fazem fronteira: {', '.join(self.__paises_fronteira)}"
