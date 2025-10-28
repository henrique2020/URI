# Problema: 1630 - Estacas     | Resposta: Accepted
# Linguagem: Python 3.11 [+1s] | Tempo: 0.000s

from math import gcd
import sys

saida = []
append = saida.append    # Overhead
for linha in sys.stdin:
    n1, n2 = map(int, linha.split())
    mdc = gcd(n1, n2)       # Máximo divisor comum
    append(str(2 * ((n1 // mdc) + (n2 // mdc))))
    
print('\n'.join(saida))
