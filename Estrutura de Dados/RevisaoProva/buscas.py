from typing import List

def busca_sequencial(vetor, chave):
    for i in range(len(vetor)):
        if vetor[i]['ip'] == chave:
            return vetor[i]['nome']
    return -1

def busca_sequencial_recursiva(vetor, chave, i=0):
    if i >= len(vetor) or vetor[i]['ip'] > chave:
        return -1
    if vetor[i]['ip'] == chave:
        return vetor[i]['nome']
    return busca_sequencial_recursiva(vetor, chave, i+1)

def busca_binaria(vetor, chave):
    primeiro = 0
    ultimo = len(vetor)-1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        if chave == vetor[meio]['ip']:
            return vetor[meio]['nome']
        elif chave < vetor[meio]['ip']:
            primeiro = meio + 1
        else:
            ultimo = meio - 1  
    return -1

def busca_binaria_recursiva(vetor: List[int], chave: int, primeiro=0, ultimo=None) -> int:
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
        return busca_binaria_recursiva(vetor, chave, primeiro, meio)
    elif chave > vetor[meio]['ip']:
        return busca_binaria_recursiva(vetor, chave, meio+1, ultimo)
    else:
        return vetor[meio]['nome']