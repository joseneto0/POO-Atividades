from pedido import Pedido
pedido = Pedido()
while True:
    tipo = int(input('Qual combustível você vai escolher? [1 - Gasolina, 2 - Etanol, 3 - Diesel] '))
    while tipo < 1 or tipo > 3:
        tipo = int(input('Tente Novamente. Qual combustível você vai escolher? [1 - Gasolina, 2 - Etanol, 3 - Diesel] '))
    tipo -= 1
    qntd = float(input('Quantos litros você quer colocar? '))
    pedido.mostrarTabela()
    pedido.entradaUsuario(tipo, qntd)
    pedido.precoPagar()
    if pedido.decrementar_bomba() == 0:
        break
    continuar = int(input('Quer continuar? [1 - SIM | 2 - NÃO] '))
    while continuar < 1 or continuar > 2:
        continuar = int(input('Tente Novamente. Quer continuar? [1 - SIM | 2 - NÃO] '))
    if continuar == 2:
        break