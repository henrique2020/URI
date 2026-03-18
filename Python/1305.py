# Problema: 1305 - Arredondamento por Valor de Corte | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]                       | Tempo: 0.024s

import sys

linhas = sys.stdin.read().splitlines()
for i in range(0, len(linhas), 2):
    num = float(linhas[i])
    cutoff = float(linhas[i + 1])
    
    result = int(num) + (1 if num % 1 >= cutoff else 0)
    print(result)
