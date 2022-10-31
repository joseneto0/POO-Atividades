from abc import ABC, abstractmethod
from typing import List

class Animal:
  def __init__(self, nome, especie):
    self.__nome = nome
    self.__especie = especie
  
  @property
  def nome(self):
    return self.__nome

  @property
  def especie(self):
    return self.__especie

class Ferramenta(ABC):

  @abstractmethod
  def filtraEspecie(self, completo: List[Animal], especieFiltrar: str):
    '''
    Recebe como parâmetro um vetor contendo animais, que podem
    ser de várias espécies diferentes, e retorna um vetor que contém
    apenas os animais cuja espécie é especificada no parâmetro
    “especieFiltrar”. Se não houver nenhum animal da espécie
    especificada, retorna um vetor com zero posições.
    '''
    pass

  @abstractmethod
  def classificaEspecies(self, completo: List[Animal]):
    '''
    Recebe como parâmetro um vetor contendo animais e retorna um
    vetor de Strings contendo o nome de todas as espécies que foram
    encontradas no vetor recebido como parâmetro. Cada nome de
    espécie só aparece uma vez no vetor de saída.
    '''
    pass

class FerramenteUso(Ferramenta):
    def filtraEspecie(self, completo: List[Animal], especieFiltrar: str):
      return [i for i in completo if i.especie == especieFiltrar]

    def classificaEspecies(self, completo: List[Animal]):
      return set([i.especie for i in completo])

class Resultado:
  def __init__(self, especie, quantidade):
    self.especie = especie
    self.quantidade = quantidade

  def __str__(self):
    return f"{self.especie} = {self.quantidade}"


class Cachorro(Animal):
  def __init__(self, nome, especie):
    super().__init__(nome, especie)

class Gato(Animal):
  def __init__(self, nome, especie):
    super().__init__(nome, especie)

class Galinha(Animal):
  def __init__(self, nome, especie):
    super().__init__(nome, especie)

class Jacare(Animal):
  def __init__(self, nome, especie):
    super().__init__(nome, especie)

class BabyShark(Animal):
  def __init__(self, nome, especie):
    super().__init__(nome, especie)

def contabilizarAnimais(animais: List[Animal], ferramenta: Ferramenta):
    l = []
    for i in ferramenta.classificaEspecies(animais):
        saida = Resultado(i, len(ferramenta.filtraEspecie(animais, i)))
        l.append(str(saida))
    return l


cachorro = Cachorro("rex", "mamifero")
gato = Gato("mimi", "mamifero")
galinha = Galinha("pintadinha", "ave")
jacare = Jacare("lacoste", "reptil")
babyShark = BabyShark("lacoste", "peixe")

ferramenta = FerramenteUso()
print(ferramenta.classificaEspecies([cachorro, gato, galinha, babyShark]))

resultado = contabilizarAnimais([cachorro, gato, galinha, jacare, babyShark], ferramenta)
print(resultado)


