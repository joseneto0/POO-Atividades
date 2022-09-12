from funcionario import *
lista = []
try:
    presidente = Presidente('Zezin', 6000.0, GrauDeFormacao.MESTRE)
    print(presidente)
    print(presidente.contraCheque())
    gerente = Gerente('Mery', 2000.0, GrauDeFormacao.DOUTOR)
    print(gerente)
    print(gerente.contraCheque())
    diretor = Diretor("Deba", 5000.0, GrauDeFormacao.DOUTOR)
    print(diretor)
    print(diretor.contraCheque())
    lista.append(presidente)
    lista.append(gerente)
    lista.append(diretor)
    print(f'''
Objeto         Funcionário        Grau de Instrução       Salário Base
============   ================   =====================   ================''')
    for i in range(len(lista)):
        print(f'{type(lista[i]).__name__:10}     {lista[i].nome:15}    {lista[i].grau:19}     R${lista[i].salario:.2f}')
    print('='*74)
except AssertionError as a:
    print(a)