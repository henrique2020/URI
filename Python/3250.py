# Problema: 3250 - Problema no Elevador | Resposta: Time limit exceeded
# Linguagem: Python 3.11 [+1s]          | Tempo: 2.000s

from collections import deque

def movimenta(a, i, o, s, d):
    visitados = [False for _ in range(a+1)]
    fila = deque([(i, 0)])
    
    while fila:
        andar, movimentos = fila.popleft()
        if andar == o:
            return movimentos
        
        movimentos += 1
        sobe = andar + s
        desce = andar - d
        
        if sobe <= andares and not visitados[sobe]:
            fila.append((sobe, movimentos))
            visitados[andar] = True
            
        if desce >= 1 and not visitados[desce]:
            fila.append((desce, movimentos))
            visitados[andar] = True
    
    return -1

andares, inicio, objetivo, sobe, desce = map(int, input().split())
movimentos = movimenta(andares, inicio, objetivo, sobe, desce)

if movimentos != -1: print(movimentos)
else: print("use the stairs")
