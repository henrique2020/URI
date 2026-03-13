# Problema: 2534 - Exame Geral | Resposta: Accepted
# Linguagem: Python 3.11 [+1s] | Tempo: 0.000s

import sys

data = sys.stdin.read().splitlines()

i = 0
while i < len(data):
    testes, q = map(int, data[i].split())
    i += 1

    notas = sorted(map(int, data[i:i+testes]), reverse=True)
    i += testes

    consultas = map(int, data[i:i+q])
    i += q

    print("\n".join(str(notas[c-1]) for c in consultas))
