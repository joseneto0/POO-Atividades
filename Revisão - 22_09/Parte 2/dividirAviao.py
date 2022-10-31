from aviao import Aviao
from data import Data
from enum import Enum

class TipoVaga(Enum):
    FUMANTE = 'F'
    NAO_FUMANTE = 'N'
    OCUPADA = 'O'

class dividirAviao(Aviao):
    def __init__(self, numero_voo, data: object, horario, numeroVagas, cadeirasFumantes, ):
        super().__init__(numero_voo, data, horario)
        self.numeroVagas = numeroVagas
        self.cadeirasFumantes = cadeirasFumantes
        self.lugares = [TipoVaga.NAO_FUMANTE.value]*(numeroVagas-cadeirasFumantes) + [TipoVaga.FUMANTE.value]*cadeirasFumantes

    @property
    def numeroVagas(self):
        return self.__numeroVagas

    @numeroVagas.setter
    def numeroVagas(self, numeroVagas):
        self.__numeroVagas = numeroVagas
        
    @property
    def cadeirasFumantes(self):
        return self.__cadeirasFumantes
    
    @cadeirasFumantes.setter
    def cadeirasFumantes(self, cadeirasFumantes):
        self.__cadeirasFumantes = cadeirasFumantes
    
    def vagasTipo(self, tipo):
        return [i+1 for i,v in enumerate(self.lugares) if v == tipo.value]

    def proximoLivrePorTipo(self, tipo: TipoVaga):
        vooLivre = self.vagasTipo(tipo)
        return vooLivre[0]

    def verifica(self, numero):
        return self.lugares[numero - 1] is not TipoVaga.OCUPADA

    def ocupa(self, numero):
        assert self.lugares[numero - 1] != TipoVaga.OCUPADA, f"Assento da posição {numero} está ocupado"
        self.lugares[numero - 1] = TipoVaga.OCUPADA

    def vagas(self):
        return [i+1 for i,v in enumerate(self.lugares) if v is not TipoVaga.OCUPADA]

try:
    d = Data('16/06/2000')
    vf = dividirAviao(133, d, '18:30', 100, 15)
    print(f"Total de vagas = {len(vf.vagas())}")
    print(f"Total de vagas para fumantes = {len(vf.vagasTipo(TipoVaga.FUMANTE))}")
    print(f"TOtal de vagas para nao-fumantes = {len(vf.vagasTipo(TipoVaga.NAO_FUMANTE))}")
    print(f"Próximo lugar livre = {vf.proximoLivre()}")
    print(f"Próximo lugar para fumante livre = {vf.proximoLivrePorTipo(TipoVaga.FUMANTE)}")
    print(f"Lugar 5 disponível = {vf.verifica(5)}")
    print(f"Lugar 10 disponível = {vf.verifica(10)}")
    print(f"Ocupar lugar 10")
    vf.ocupa(10)
    print(f"Lugar 10 disponível = {vf.verifica(10)}")
    print("ocupa 1, 2, 3")
    vf.ocupa(1)
    vf.ocupa(2)
    vf.ocupa(3)
    print(f"Próximo lugar livre = {vf.proximoLivre()}")
    print("Ocupa 71 e 72")
    vf.ocupa(71)
    vf.ocupa(72)
    print(f"Próximo lugar livre para fumante = {vf.proximoLivrePorTipo(TipoVaga.FUMANTE)}")
    print(f"Vagas = {vf.vagas()}")
except AssertionError as e:
    print(e)

    