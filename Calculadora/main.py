from calculadora import Calculadora
calc = Calculadora()
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
    print('(e) sair')
    print('-' * 20)
    operacao = input("Operação: ").lower()
    print('-' * 20)
    calc.getOperacao(operacao)
    if operacao == '+':
        num = float(input('Digite o número para a realização da operação: '))
        calc.novoNumero(num)
        o = calc.adicionar()
        valor = calc.numeroAtual(o)
    elif operacao == '-':
        num = float(input('Digite o número para a realização da operação: '))
        calc.novoNumero(num)
        o = calc.subtrair()
        valor = calc.numeroAtual(o)
    elif operacao == '/':
        num = float(input('Digite o número para a realização da operação: '))
        calc.novoNumero(num)
        o = calc.divisao()
        valor = calc.numeroAtual(o)
    elif operacao == '*':
        num = float(input('Digite o número para a realização da operação: '))
        calc.novoNumero(num)
        o = calc.multiplicacao()
        valor = calc.numeroAtual(o)
    elif operacao == 'r':
        calc.numeroAtual(0)
    elif operacao == 'd':
        a = calc.desfazer()
        calc.numeroAtual(a)
    elif operacao == 'e':
        break