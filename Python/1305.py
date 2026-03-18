# Problema: 1305 - Arredondamento por Valor de Corte | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]                       | Tempo: 0.218

import sys

linhas = sys.stdin.read().splitlines()
while linhas:
    num = float(linhas.pop(0))
    cutoff = float(linhas.pop(0))
    
    inteiro = int(num // 1)
    decimal = num - inteiro
    if decimal >= cutoff:
        inteiro += 1
        
    print(inteiro)
