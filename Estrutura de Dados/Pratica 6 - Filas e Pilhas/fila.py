class No:
    def __init__(self, carga, proximo = None):
        self.carga = carga
        self.proximo = proximo

class Fila:
    def __init__(self):
        self.fim = None
        self.inicio = None

    def add(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.fim
        self.fim = novo_no

    def __str__(self):
        s = ''
        atual = self.fim
        while atual is not None:
            if atual.proximo is not None:
                s += str(atual.carga) + '\n'
            else:
                s += str(atual.carga)
            atual = atual.proximo
        return s

if __name__ == '__main__':
    fila = Fila()
    fila.add(50)
    fila.add(20)
    print(fila)
    fila.remove()
    print(fila)