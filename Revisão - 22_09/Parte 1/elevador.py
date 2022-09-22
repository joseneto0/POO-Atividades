class Elevador:
    def __init__(self, total_andares, capacidade, pessoas_presentes=0, andar_atual=0):
       self.andar_atual = andar_atual
       self.total_andares = total_andares
       self.capacidade = capacidade
       self.pessoas_presentes = pessoas_presentes

    @property
    def andar_atual(self):
        return self.__andar_atual

    @andar_atual.setter
    def andar_atual(self, andar_atual):
        self.__andar_atual = andar_atual

    @property
    def total_andares(self):
        return self.__total_andares

    @total_andares.setter
    def total_andares(self, total_andares):
        self.__total_andares = total_andares

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade):
        self.__capacidade = capacidade

    @property
    def pessoas_presentes(self):
        return self.__pessoas_presentes

    @pessoas_presentes.setter
    def pessoas_presentes(self, pessoas_presentes):
        self.__pessoas_presentes = pessoas_presentes

    def entra(self):
        if self.pessoas_presentes < self.capacidade:
            self.pessoas_presentes += 1
            return 'Mais uma pessoa entrou no elevador!'
        return 'Não foi possível entrar, poís o elevador está cheio!'
    
    def sai(self):
        if self.pessoas_presentes > 0:
            self.pessoas_presentes -= 1
            return 'Uma pessoa saiu do elevador'
        return "Não tem ninguém presente no elevador, logo, não é possível 'sair'"

    def sobe(self):
        if self.andar_atual < self.total_andares:
            self.andar_atual += 1
            return f'Você subiu 1 andar. Agora você está no andar {self.andar_atual}'
        return 'Você já está no topo no Prédio, não é possível subir mais'
    
    def desce(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            return f'Você desceu 1 andar. Agora você está no andar {self.andar_atual}'
        return 'Você está no térreo do prédio, não é possível descer mais'

    def __str__(self):
        return f'Estamos no andar {self.andar_atual} com {self.pessoas_presentes} pessoas presentes'

if __name__ == '__main__':
    elevador = Elevador(10, 12, 10)
    print(elevador)
    print(elevador.sobe())
    print(elevador)
    print(elevador.desce())
    print(elevador.desce())
    print(elevador)
    elevador.entra()
    print(elevador)
    elevador.sai()
    print(elevador)
    print(elevador.sobe())
    print(elevador)