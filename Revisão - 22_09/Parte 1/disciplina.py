class Disciplina:
    def __init__(self, matricula: int, nome: str, notas_prova: list, nota_trabalho: float):
        self.matricula = matricula
        self.nome = nome
        self.notas_prova = notas_prova
        self.nota_trabalho = nota_trabalho

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        assert type(matricula) == int, "Digite a matricula como número inteiro"
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        assert type(nome) == str and nome.isalpha(), "Nome Inválido"
        self.__nome = nome

    @property
    def notas_prova(self):
        return self.__notas_prova

    @notas_prova.setter
    def notas_prova(self, notas_prova):
        assert type(notas_prova) == list, "Coloque as notas em uma lista :D"
        assert len(notas_prova) == 2, "Você só teve 2 provas, não coloque mais notas que isso :)"
        self.__notas_prova = notas_prova

    @property
    def nota_trabalho(self):
        return self.__nota_trabalho

    @nota_trabalho.setter
    def nota_trabalho(self, nota_trabalho):
        assert type(nota_trabalho) == int or type(nota_trabalho) == float, "Utilize o tipo inteiro ou flutuante (int/float) para a nota do trabalho"
        self.__nota_trabalho = nota_trabalho

    def media(self):
        media = 0
        for i in self.notas_prova:
            media += (i * 2.5)
        media += (self.nota_trabalho * 2)
        media /= 7
        return round(media, 2)

    def calcula_final(self):
        if self.media() < 7:
            return f'Você precisa de {7 - self.media()} para passar :(\nVocê está na Prova Final'
        return "Você foi Aprovado :)"
if __name__ == '__main__':
    try:
        zezin = Disciplina(202131234123, 'Zezin', [8, 8], 2)
        print(f'{zezin.__class__.__name__} do {zezin.nome}')
        print(zezin.media())
        print(zezin.calcula_final())
        tanj = Disciplina(201203102301, 'Tanjiro', [10, 10], 6)
        print()
        print(f'{tanj.__class__.__name__} do {tanj.nome}')
        print(tanj.media())
        print(tanj.calcula_final())
    except AssertionError as erro:
        print(erro)