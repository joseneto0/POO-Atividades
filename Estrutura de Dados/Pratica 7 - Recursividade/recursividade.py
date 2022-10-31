def contem_par(lista, ponteiro=0):
    if ponteiro >= len(lista):
        return False
    if lista[ponteiro] % 2 == 0:
        return True
    return contem_par(lista, ponteiro+1)

def todos_impares(lista, ponteiro=0):
    if ponteiro >= len(lista):
        return True
    if lista[ponteiro] % 2 == 0:
        return False
    return todos_impares(lista, ponteiro+1)

def pos_max(lista, ponteiro=0, index_max=0, maior=0):
    if ponteiro >= len(lista):
        return index_max
    if lista[ponteiro] > maior:
        maior = lista[ponteiro]
        index_max = ponteiro
    return pos_max(lista, ponteiro+1, index_max, maior)

def inverter_lista(lista, lista_invertida=[]):
    if len(lista) == 0:
        return lista_invertida
    lista_invertida.append(lista.pop())
    return inverter_lista(lista, lista_invertida)

def lista_igual(lista1, lista2, c=0):
    if len(lista1) != len(lista2):
        return False
    if c >= len(lista1) or c >= len(lista2):
        return True
    if lista1[c] != lista2[c]:
        return False
    return lista_igual(lista1, lista2, c+1)

lista_par = [1, 2, 4, 6, 9]
lista_impar = [1, 1, 1, 3, 5]
print(contem_par(lista_par))
print(todos_impares(lista_impar))

lista = [1, 2, 3, 4, 5, 8, 7, 10, 20, 30 ,40]

print(inverter_lista(lista.copy()))

lista2 = [1, 2, 3, 4, 5, 8, 7, 10, 20, 30]
lista3 = [1, 2, 3, 4, 5, 8, 7, 10, 20, 30]
print(lista_igual(lista2, lista3))

lista_maior = [1, 10, 50, 2000, 30, 10]
print(pos_max(lista_maior))