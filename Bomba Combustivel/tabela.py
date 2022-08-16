class Tabela:
    def __init__(self, tamanho = 40):
        self.tamanho = tamanho
        self.precos = [5.49, 4.77, 7.96]
        self.qntd_litros_bomba = 10000

    def mostrarTabela(self):
        print('=' * self.tamanho)
        print('POSTO DO ZEZÉ'.center(self.tamanho))
        print(f'Gasolina: R$ {self.precos[0]}'.center(self.tamanho))
        print(f'Etanol: R$ {self.precos[1]}'.center(self.tamanho))
        print(f'Preco Diesel: R$ {self.precos[2]}'.center(self.tamanho))
        print(f'Litros disponíveis na bomba: {self.qntd_litros_bomba} L'.center(self.tamanho))
        print('=' * self.tamanho)