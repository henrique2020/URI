# Problema: 2159 - Número Aproximado de Primos  | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]                  |Tempo: 0.000s

from math import log

n = int(input())
minimo = n / log(n)
maximo = 1.25506*minimo
print(f"{minimo:.1f} {maximo:.1f}")