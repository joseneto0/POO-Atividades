from random import randint
class No:
    def __init__(self, carga, anterior=None, proximo=None):
        self.carga = carga
        self.anterior = anterior
        self.proximo = proximo

    def __str__(self):
        return str(self.carga)

class FilaCircular:
    def __init__(self):
        self.cauda = None
        self.cabeca = None

    def inserir(self, valor):
        novo_no = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo_no
        else:
            novo_no.anterior = self.cauda
            novo_no.anterior.proximo = novo_no
            self.cauda = novo_no
            self.cauda.proximo = self.cabeca
            self.cabeca.anterior = self.cauda

    def remover(self):
        if self.cabeca is None:
            print('Lista Vazia')
            return
        if self.cabeca is self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cabeca = self.cabeca.proximo
            self.cabeca.anterior = self.cauda
            self.cauda.proximo = self.cabeca

    def imprimir(self):
        atual = self.cabeca
        if atual is None:
            print('Lista Vazia')
            return
        while atual is not self.cauda:
            print(atual)
            atual = atual.proximo
        print(atual)

    def executar(self, n):
        if self.cabeca is None:
            print('Lista Vazia')
            return
        else:
            atual = self.cabeca
            while n > 0:
                print(atual)
                atual = atual.proximo
                n -= 1

    def __len__(self):
        i = 0
        if self.cabeca is None:
            return 0
        else:
            atual = self.cabeca
            while atual is not self.cauda:
                atual = atual.proximo
                i += 1
            return i + 1

fila = FilaCircular()
for i in range(50):
    fila.inserir(randint(1, 50))
print('----')
fila.imprimir()
print('###')
fila.executar(20)