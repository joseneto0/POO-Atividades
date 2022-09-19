from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome: str, endereco: str, telefone: str):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        assert type(nome) == str and nome.isalpha() == True, f"Digite um nome válido. Nome inválido: {nome}"
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        assert type(endereco) == str, f"Digite um endereço válido. Endereço Inválido: {endereco}"
        self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        assert type(telefone) == str, f"Digite o telefone como string. Telefone Inválido: {telefone}"
        self.__telefone = telefone

class Fornecedor(Pessoa):
    def __init__(self, nome: str, endereco: str, telefone: str, valorCredito: float, valorDivida: float):
        super().__init__(nome, endereco, telefone)
        self.valorCredito = valorCredito
        self.valorDivida = valorDivida

    @property
    def valorCredito(self):
        return self.__valorCredito

    @valorCredito.setter
    def valorCredito(self, valorCredito):
        assert type(valorCredito) == float and valorCredito > 0, f"Valor incorreto (float) ou menor que zero. Valor Incorreto: {valorCredito}"
        self.__valorCredito = valorCredito
    
    @property
    def valorDivida(self):
        return self.__valorDivida

    @valorDivida.setter
    def valorDivida(self, valorDivida):
        assert type(valorDivida) == float and valorDivida > 0, f"Valor incorreto (float) ou menor que zero. Valor Incorreto: {valorDivida}"
        self.__valorDivida = valorDivida

    def obterSaldo(self):
        return f"Voce tem R$ {self.valorCredito - self.valorDivida} de saldo"

class Empregado(Pessoa):
    def __init__(self, nome: str, endereco: str, telefone: str, codigoSetor: int, salarioBase: float, imposto: int, comissao: int):
        super().__init__(nome, endereco, telefone)
        self.codigoSetor = codigoSetor
        self.salarioBase = salarioBase
        self.imposto = imposto
        self.comissao = comissao

    @property
    def codigoSetor(self):
        return self.__codigoSetor

    @codigoSetor.setter
    def codigoSetor(self, codigoSetor):
        assert type(codigoSetor) == int, f"Digite um número inteiro. Número Inválido: {codigoSetor}"
        self.__codigoSetor = codigoSetor

    @property
    def salarioBase(self):
        return self.__salarioBase

    @salarioBase.setter
    def salarioBase(self, salarioBase):
        assert type(salarioBase) == float, f"Digite o valor como float. Salário Inválido: {salarioBase}"
        assert salarioBase > 0, "Digite um salário base maior que 0"
        self.__salarioBase = salarioBase

    @property
    def imposto(self):
        return self.__imposto

    @imposto.setter
    def imposto(self, imposto):
        assert type(imposto) == int, "Digite um valor inteiro para o Imposto"
        assert imposto >= 0 and imposto <= 100, "Valor do Imposto fora dos intervalos permitidos [0 - 100]"
        self.__imposto = imposto / 100

    @property
    def comissao(self):
        return self.__comissao

    @comissao.setter
    def comissao(self, comissao):
        assert type(comissao) == int, "Digite um valor inteiro para a comissão"
        assert comissao >= 0 and comissao <= 100, "Valor da Comissão fora dos intervalos permitidos [0 - 100]"
        self.__comissao = comissao / 100

    @abstractmethod
    def calcularSalario(self):
        return self.salarioBase - (self.salarioBase * self.imposto)

class Administrador(Empregado):
    def __init__(self, nome: str, endereco: str, telefone: str, codigoSetor: int, salarioBase: float, imposto: int, ajudaDeCusto: float, comissao=0):
        super().__init__(nome, endereco, telefone, codigoSetor, salarioBase, imposto, comissao)
        self.ajudaDeCusto = ajudaDeCusto

    @property
    def ajudaDeCusto(self):
        return self.__ajudaDeCusto

    @ajudaDeCusto.setter
    def ajudaDeCusto(self, ajudaDeCusto):
        assert type(ajudaDeCusto) == float or type(ajudaDeCusto) == int, f'Digite um valor para a ajuda de custo com tipo float/int. Valor Inválido: {ajudaDeCusto}'
        self.__ajudaDeCusto = ajudaDeCusto

    def calcularSalario(self):
        return super().calcularSalario() + self.ajudaDeCusto

class Operario(Empregado):
    def __init__(self, nome: str, endereco: str, telefone: str, codigoSetor: int, salarioBase: float, imposto: int, valorProducao: int, comissao: int):
        super().__init__(nome, endereco, telefone, codigoSetor, salarioBase, imposto, comissao)
        self.valorProducao = valorProducao

    @property
    def valorProducao(self):
        return self.__valorProducao

    @valorProducao.setter
    def valorProducao(self, valorProducao):
        assert type(valorProducao) == float or type(valorProducao) == int, f'Digite um valor para o valor da produção com tipo float/int. Valor Inválido: {valorProducao}'
        self.__valorProducao = valorProducao

    def calcularSalario(self):
        return super().calcularSalario() + (self.valorProducao * self.comissao)

class Vendedor(Empregado):
    def __init__(self, nome: str, endereco: str, telefone: str, codigoSetor: int, salarioBase: float, imposto: int, comissao: int, valorVendas: float):
        super().__init__(nome, endereco, telefone, codigoSetor, salarioBase, imposto, comissao)
        self.valorVendas = valorVendas

    @property
    def valorVendas(self):
        return self.__valorVendas

    @valorVendas.setter
    def valorVendas(self, valorVendas):
        assert type(valorVendas) == float or type(valorVendas) == int, f'Digite um valor para o valor das Vendas com tipo float/int. Valor Inválido: {valorVendas}'
        self.__valorVendas = valorVendas

    def calcularSalario(self):
        return super().calcularSalario() + (self.valorVendas * self.comissao)