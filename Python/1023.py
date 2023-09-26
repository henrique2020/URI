from math import floor, trunc
from sys import stdin

cidade = 0
while True:
    casas = int(stdin.readline())
    if casas == 0: break
    
    cidade += 1
    habitantes = 0
    m3 = 0
    consumo_habitante = {}
    for x in range(casas):
        moradores, consumo = map(int, stdin.readline().split())
        habitantes += moradores
        m3 += consumo
        
        consumo_morador = floor(consumo/moradores)
        consumo_habitante.setdefault(consumo_morador, 0)
        consumo_habitante[consumo_morador] += moradores
    
    media = (trunc((m3 / habitantes)*100))/100

    print(f'Cidade# {cidade}:')
    print(' '.join([f'{value}-{key}' for key, value in sorted(consumo_habitante.items())]))
    print(f'Consumo medio: {media:0.2f} m3.\n')