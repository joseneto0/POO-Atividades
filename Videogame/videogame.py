from datetime import date
class Videogame:
    numero_de_serie = 0
    def __init__(self, data = date.today(), marca = 'Indisponivel', modelo = 'Indisponivel', hd = '1 TB', garantia = '1 ano'):
      self.data = data
      self.marca = marca
      self.modelo = modelo
      self.hd = hd
      self.jogos = []
      self.garantia = garantia
      self.numSerie = self.incrementar_num_serie()
    
    def __str__(self):
        return f'Você tem o videogame {self.modelo} com número de série {self.numSerie} da marca {self.marca}, fabricado em {self.data}, e você tem {self.jogos} de jogos'

    def incrementar_num_serie(self):
      Videogame.numero_de_serie += 1
      return Videogame.numero_de_serie
    
    def instalar_jogos(self, jogos):
      string = ''
      for i in range(len(jogos)):
        if i < len(jogos)-1:
          string += jogos[i] + ',' + ' '
        else:
          string += jogos[i]
      self.jogos = string