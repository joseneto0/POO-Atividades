from tabela import Tabela
from time import sleep
class Pedido(Tabela):
    def __init__(self):
        super().__init__()

    def entradaUsuario(self, tipo, qntd):
        self.combustivel = tipo
        self.nomesCombustivel = ['Gasolina', 'Etanol', 'Diesel']
        self.litros = qntd
    
    def decrementar_bomba(self):
        self.qntd_litros_bomba -= self.litros
        if self.qntd_litros_bomba < 0:
            self.qntd_litros_bomba = 0
        return self.qntd_litros_bomba
    
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

    def linhas(self):
        print('=' * self.tamanho)