#Time Limit Exceded
from math import floor, trunc

cidade = 0
while True:
    casas = int(input())
    if casas == 0: break
    
    cidade += 1
    habitantes = 0
    m3 = 0
    consumo_habitante = {}
    for x in range(casas):
        moradores, consumo = map(int, input().split())
        habitantes += moradores
        m3 += consumo
        
        consumo_morador = floor(consumo/moradores)
        consumo_habitante.setdefault(consumo_morador, 0)
        consumo_habitante[consumo_morador] += moradores
        #if consumo_morador not in consumo_habitante: consumo_habitante[consumo_morador] = moradores
        #else: consumo_habitante[consumo_morador] += moradores
    
    media = (trunc((m3 / habitantes)*100))/100
    ordem_consumo = ''
    '''
    consumos = sorted(consumo_habitante.items())
    for key, value in consumos:
        ordem_consumo += f'{value}-{key} '
    ordem_consumo.lstrip()
    '''
    print(f'Cidade# {cidade}:')
    #print(ordem_consumo)
    print(' '.join([f'{value}-{key}' for key, value in sorted(consumo_habitante.items())]))
    print(f'Consumo medio: {media:0.2f} m3.')
    print()
