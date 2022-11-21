from typing import List

def selection_sort_alg(dicio: List):
    for i in range(len(dicio)):
        pos_menor = i
        menor = dicio[i]
        for j in range(i+1, len(dicio)):
            if dicio[j]['ip'] < menor['ip']:
                menor = dicio[j]
                pos_menor = j
        dicio[pos_menor] = dicio[i]
        dicio[i] = menor

def busca_binaria_recursiva1(vetor: List[int], chave: int, primeiro=0, ultimo=None) -> int:
    if ultimo is None:
        ultimo = len(vetor)-1

    if primeiro == ultimo:
        if vetor[primeiro]['ip'] > chave:
            return primeiro
        else:
            return primeiro + 1

    if primeiro > ultimo:
        return primeiro

    meio = (primeiro + ultimo) // 2 

    if chave < vetor[meio]['ip']: 
        return busca_binaria_recursiva1(vetor, chave, primeiro, meio)
    elif chave > vetor[meio]['ip']:
        return busca_binaria_recursiva1(vetor, chave, meio+1, ultimo)
    else:
        return meio

def insertion_sort_bin(lista: List):
    for i in range (1, len(lista)):
        chave = lista[i]
        j = i - 1
        loc = busca_binaria_recursiva1(lista, chave['ip'])
        while j >= loc:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = chave

def merge(esquerda, direita, lista):
    i, j, k = 0,0,0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i]['ip'] <= direita[j]['ip']:
            lista[k] = esquerda[i]
            i += 1
            k += 1
        else:
            lista[k] = direita[j]
            j += 1
            k += 1
    
    while i < len(esquerda):
        lista[k] = esquerda[i]
        i += 1
        j += 1
    
    while j < len(direita):
        lista[k] = direita[j]
        j += 1
        k += 1

def mergesort(lista):
    if len(lista) < 2:
        return lista
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]
    mergesort(esquerda)
    mergesort(direita)
    merge(esquerda, direita, lista)

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]['ip']
    menores = [i for i in lista if i['ip'] < pivo]
    iguais = [i for i in lista if i['ip'] == pivo]
    maiores = [i for i in lista if i['ip'] > pivo]
    return quicksort(menores) + iguais + quicksort(maiores)