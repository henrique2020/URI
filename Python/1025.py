# Problema: 1025 - Onde está o Mármore? | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]          | Tempo: 0.365s

from sys import stdin
import bisect

caso = 0
while True:
    n, q = map(int, stdin.readline().split())
    if n == 0 and q == 0:
        break

    marmores = sorted(int(stdin.readline()) for _ in range(n))
    caso += 1
    print(f"CASE# {caso}:")

    for _ in range(q):
        procura = int(stdin.readline())
        pos = bisect.bisect_left(marmores, procura)  # busca binária

        # verifica se encontrou
        if pos < len(marmores) and marmores[pos] == procura:
            print(f"{procura} found at {pos + 1}")
        else:
            print(f"{procura} not found")