from pessoa import *
try:
    lista = []
    f = Fornecedor('Zezin', 'Rua Arnaldo Gomes', '8154-3041', 50000.00, 25000.00)
    f.endereco = 'Rua do Zezo'

    adm = Administrador('Orlando', 'Orlando 2', '123123123131', 12315213231, 2000.20, 20, 500)
    lista.append(adm)

    operario = Operario('Boninoro', 'Rua Lava Jato', '695412311', 123151231231, 3000.00, 30, 2000, 60)
    lista.append(operario)

    print(f'Fornecedor: {f.nome}')
    print(f.obterSaldo())
    print()
    for i in lista:
        print(i.__class__.__name__)
        print(f'Salário: R$ {i.calcularSalario():.2f}')
except AssertionError as erro:
    print(erro)