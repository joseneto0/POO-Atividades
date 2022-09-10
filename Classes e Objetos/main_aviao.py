from aviao import *
try:
    aviao1 = Aviao(12314, '10/06/2001', '18:35')
    print(aviao1.numero_voo)
    print(aviao1.data)
    print(aviao1.horario)
    print(aviao1.getAssento)
    print(aviao1.ocupar(1))
    print(aviao1.getAssento)
    print(aviao1.ocupar(100))
    print(aviao1.estaDisponivel(100))
    print(aviao1)
except AssertionError as a:
    print(a)