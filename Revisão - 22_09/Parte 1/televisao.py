class Televisao:
    def __init__(self):
        self.canal_atual = 1
        self.volume = 10
    
class ControleRemoto:
    def __init__(self, objeto: object) -> None:
        self.objeto = objeto

    @property
    def objeto(self):
        return self.__objeto

    @objeto.setter
    def objeto(self, objeto):
        self.__objeto = objeto

    def aumentar_volume(self):
        if self.objeto.volume < 100:
            self.objeto.volume += 1
            return 'O volume foi aumentado em 1'
        return 'O Volume já está no máximo'

    def diminuir_volume(self):
        if self.objeto.volume > 0:
            self.objeto.volume -= 1
            return 'O Volume foi diminuido em 1'
        return 'O Volume já está no mínimo'

    def aumentar_canal(self):
        self.objeto.canal_atual += 1
        return 'O Canal foi aumentado em 1'

    def diminuir_canal(self):
        self.objeto.canal_atual -= 1
        return 'O Canal foi diminuido em 1'

    def trocar_canal(self, canal):
        self.objeto.canal_atual = canal
        return f'O canal foi alterado para o {canal}'

    def consulta(self):
        return f"O canal atual é o {self.objeto.canal_atual} e o volume atual é {self.objeto.volume}"
    
    
if __name__ == '__main__':
    tv = Televisao()
    controle = ControleRemoto(tv)
    controle.aumentar_volume()
    print(controle.consulta())
    controle.diminuir_volume()
    controle.diminuir_volume()
    controle.diminuir_volume()
    controle.diminuir_volume()
    print(controle.consulta())
    print(controle.trocar_canal(5))
    print(controle.consulta())