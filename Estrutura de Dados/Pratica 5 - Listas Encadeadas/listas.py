class No:
    def __init__(self, carga, prox = None):
        self.carga = carga
        self.prox = prox

    def __str__(self):
        return str(self.carga)

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def inserir_no_inicio(self, valor):
        novo_no = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo_no
        else:
            novo_no.prox = self.cabeca
            self.cabeca = novo_no

    def inserir_no_final(self, valor):
        novo_no = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo_no
        else:
            self.cauda.prox = novo_no
            self.cauda = novo_no

    def remover_do_inicio(self):
        if self.cabeca is None:
            print('Lista Vazia')
            return
        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cabeca = self.cabeca.prox

    def remover_do_final(self):
        if self.cabeca is None:
            print('Lista Vazia')
            return
        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            atual = self.cabeca
            while atual is not self.cauda:
                atual = atual.prox

            self.cauda = self.cabeca
            self.cabeca.prox = None

    def imprimir_lista(self):
        if self.cabeca is None:
            print("A lista está vazia :O")
            return
        atual = self.cabeca
        while atual is not None:
            print(atual.carga)
            atual = atual.prox
            
class ListaEncadeadaEstendida(ListaEncadeada):
    def __init__(self):
        super().__init__()

    def pares(self):
        atual = self.cabeca
        while atual is not None:
            if atual.carga % 2 == 0:
                print(atual.carga)
            atual = atual.prox

    def impares(self):
        atual = self.cabeca
        while atual is not None:
            if atual.carga % 2 != 0:
                print(atual.carga)
            atual = atual.prox

    def buscar_pos(self, valor):
        atual = self.cabeca
        i = 0
        while atual is not None:
            if atual.carga == valor:
                print(f'Posição: {i}')
                return
            atual = atual.prox
            i += 1
        print(-1)

if __name__ == '__main__':
    l = ListaEncadeada()
    l.inserir_no_inicio(5)
    l.inserir_no_final(1)
    l.inserir_no_final(7)
    l.inserir_no_final(4)
    l.inserir_no_final(8)
    l.imprimir_lista()
    print(l.cauda.prox)
    print()
    l_ext = ListaEncadeadaEstendida()
    l_ext.inserir_no_final(10)
    l_ext.inserir_no_final(5)
    l_ext.inserir_no_final(2)
    l_ext.inserir_no_final(9)
    l_ext.inserir_no_final(10)
    l_ext.inserir_no_final(10)
    l_ext.inserir_no_final(10)
    l_ext.inserir_no_final(10)
    l_ext.pares()
    print('-')
    l_ext.impares()
    print()
    l_ext.buscar_pos(5)
    l_ext.buscar_pos(10)
    l_ext.buscar_pos(100)
    print()
    l_ext.imprimir_lista()
    print()
    print(l_ext.inserir_pos(4, 30))
    l_ext.imprimir_lista()
    print(l_ext.inserir_pos(6, 30))
    print()
    l_ext.imprimir_lista()