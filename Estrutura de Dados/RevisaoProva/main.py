from ordenacao import *
from buscas import *
from PilhaCircular import *

import csv
from typing import List

servidores_dns = []
with open('dns_br.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    next(csv_reader, None)  # pula os cabeçalhos
    for row in csv_reader:
        servidor_dns = dict()
        servidor_dns['ip'] = row[0]
        servidor_dns['nome'] = row[1]
        servidores_dns.append(servidor_dns)

servidores_selection = servidores_dns.copy()
selection_sort_alg(servidores_selection)
#print(servidores_selection)

servidores_insertion = servidores_dns.copy()
insertion_sort_bin(servidores_insertion)
#print(servidores_insertion)

servidores_merge = servidores_dns.copy()
mergesort(servidores_merge)
#print(servidores_merge)

servidores_quick = servidores_dns.copy()
quicksort(servidores_quick)
#print(servidores_quick)

print(busca_sequencial(servidores_insertion, '189.42.239.34'))
print(busca_sequencial_recursiva(servidores_merge, '189.42.239.34'))
print(busca_binaria(servidores_quick, '189.42.239.34'))
print(busca_binaria_recursiva(servidores_selection, '189.42.239.34'))


