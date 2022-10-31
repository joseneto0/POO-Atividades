class No:
    def __init__(self, carga, anterior = None):
        self.carga = carga
        self.anterior = anterior

class Pilha:
    def __init__(self):
        self.topo = None

    def push(self, valor):
        novo_no = No(valor)
        novo_no.anterior = self.topo
        self.topo = novo_no

    def pop(self):
        if self.topo == None:
            return "A pilha está vazia"
        retornar = self.topo.carga
        self.topo = self.topo.anterior
        return retornar

    def __str__(self):
        s = ''
        atual = self.topo
        while atual is not None:
            if atual.anterior is not None:
                s += str(atual.carga) + '\n'
            else:
                s += str(atual.carga)
            atual = atual.anterior
        return s

    def is_empty(self):
        atual = self.topo
        while atual is not None:
            if atual.carga is not None:
                return False
        return True

    def remover_ate_elemento(self, elemento):
        atual = self.topo
        while atual is not None:
            if atual.carga == elemento:
                self.pop()
                return f"Elementos até {elemento} retirados"
            else:
                self.pop()
            atual = atual.anterior
        return f"Todos os elementos foram removidos, {elemento} não foi encontrado"

    def is_palindrome(self, string):
        string_reversa = string[::-1]
        string_reversa = string_reversa.replace(" ", "")
        string_normal = string.replace(" ", "")
        if string_normal == string_reversa:
            return True
        return False
        
if __name__ == '__main__':
    pilha = Pilha()
    pilha.push(44)
    pilha.push(65)
    pilha.push(32)
    pilha.push(54)
    print(pilha)
    print(pilha.remover_ate_elemento(65))
    print(pilha)
    print(pilha.is_empty())
    print(pilha.is_palindrome("socorram me subi no onibus em marrocos"))
    