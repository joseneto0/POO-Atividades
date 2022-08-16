from time import sleep
class Calculadora:
    def __init__(self, valor = None):
        if valor == None:
            self.__valor = 0
        else:
            self.__valor = valor
    
    def getOperacao(self, operacao):
        self.__operacao = operacao

    def __del__(self):
        if self.__operacao == 'e':
            print('Obrigado pelo Uso :D')
            print('Encerrando processo em: ')
            for i in range(3, 0, -1):
                print(f'{i}', end=' ', flush=True)
                sleep(1)
            print('FIM')
        
    def numeroAtual(self, numAtual):
        self.__numeroAntigo = self.__valor
        self.__valor = numAtual
        return numAtual
        
    def registrador(self):
        return self.__valor
    
    def novoNumero(self, num):
        self.__valorNovo = num
    
    def adicionar(self):
        adicao = self.__valor + self.__valorNovo
        return adicao 

    def subtrair(self):
        subtracao = self.__valor - self.__valorNovo
        return subtracao

    def divisao(self):
        divisao = self.__valor / self.__valorNovo
        return divisao

    def multiplicacao(self):
        multiplicacao = self.__valor * self.__valorNovo
        return multiplicacao

    def desfazer(self):
        return self.__numeroAntigo