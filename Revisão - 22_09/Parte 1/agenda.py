from pessoa import Pessoa
class Agenda:
    def __init__(self) -> None:
        self.lista = []
    
    def armazenaPessoa(self, objeto: object):
        self.lista.append([objeto.nome, objeto.data, objeto.altura])
        
    def imprimeAgenda(self):
        return self.lista
    
    def removePessoa(self, nome: str):
        for i in range(len(self.lista)):
            if nome in self.lista[i][0]:
                del self.lista[i]
                return 'Usuário Deletado :)'
        return 'Usuário nao encontrado :O' 
    
    def buscaPessoa(self, nome: str):
        for i in range(len(self.lista)):
            if nome in self.lista[i][0]:
                return f'Usuário encontrado na Agenda na posicao {i+1} :)'
        return 'Usuário nao encontrado :('
    
    def imprimePessoa(self, index: str):
        if int(index) - 1 < len(self.lista):
            return self.lista[int(index)-1]
        else:
            return 'Nenhum usuário cadastrado nessa posição :c'
        
if __name__ == '__main__':
    try:
        p = Pessoa('José', '16/06/2004', 1.73) 
        p1 = Pessoa('Mary', '23/11/2001', 1.65) 
        agenda = Agenda()
        agenda.armazenaPessoa(p)
        print(agenda.imprimeAgenda())
        agenda.armazenaPessoa(p1)
        print(agenda.imprimeAgenda())
        agenda.removePessoa('José')
        print(agenda.imprimeAgenda())
        print(agenda.buscaPessoa('José'))
        print(agenda.buscaPessoa('Joseee'))
        print(agenda.imprimePessoa('1'))
    except AssertionError as erro:
        print(erro)