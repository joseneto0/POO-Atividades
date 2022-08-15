from calculadora import Calculadora
calc = 0
valor = float(input('Digite o valor inicial: '))
calc = Calculadora(valor)
while True:
    print('-' * 20)
    print('Calculadora do Zezin'.center(15))
    print('+' + '-' * 18 + '+')
    print(f'|{calc.registrador():9}         |')
    print('+' + '-' * 18 + '+')
    print('(+) somar')
    print('(-) subtrair')
    print('(/) dividir')
    print('(*) multiplicar')
    print('(r) resetar')
    print('(d) desfazer')
    print('(e) - sair')
    print('-' * 20)
    operacao = input("Operação: ").lower()
    print('-' * 20)
    calc.getOperacao(operacao)
    if operacao == '+':
        calc.novoNumero()
        o = calc.adicionar()
        valor = calc.numeroAtual(o)
    elif operacao == '-':
        calc.novoNumero()
        o = calc.subtrair()
        valor = calc.numeroAtual(o)
    elif operacao == '/':
        calc.novoNumero()
        o = calc.divisao()
        valor = calc.numeroAtual(o)
    elif operacao == '*':
        calc.novoNumero()
        o = calc.multiplicacao()
        valor = calc.numeroAtual(o)
    elif operacao == 'r':
        calc.numeroAtual(0)
    elif operacao == 'd':
        a = calc.desfazer()
        calc.numeroAtual(a)
    elif operacao == 'e':
        break