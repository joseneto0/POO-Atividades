from tabela import Tabela
from time import sleep
class Pedido(Tabela):
    def __init__(self):
        super().__init__()

    def entradaUsuario(self):
        tipo = int(input('Qual combustível você vai escolher? [1 - Gasolina, 2 - Etanol, 3 - Diesel] '))
        while tipo < 1 or tipo > 3:
            tipo = int(input('Tente Novamente. Qual combustível você vai escolher? [1 - Gasolina, 2 - Etanol, 3 - Diesel] '))
        tipo -= 1
        self.combustivel = tipo
        self.nomesCombustivel = ['Gasolina', 'Etanol', 'Diesel']
        qntd = float(input('Quantos litros você quer colocar? '))
        self.litros = qntd

    def linhas(self):
        print('=' * self.tamanho)
    
    def precoPagar(self):
        sleep(1)
        self.linhas()
        print(f'Você abasteceu {self.litros} litros de {self.nomesCombustivel[self.combustivel]}'.center(self.tamanho))
        sleep(1)
        print(f'Sua conta deu: '.center(self.tamanho))
        for i in range(40):
            print('-', end='', flush=True)
            sleep(0.1)
        print()
        print(f'R$ {self.litros * self.precos[self.combustivel]:.2f}'.center(self.tamanho))
        self.linhas()