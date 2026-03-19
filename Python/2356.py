# Problema: 2356 - Bactéria I  | Resposta: Accepted
# Linguagem: Python 3.11 [+1s] | Tempo: 0.000s

import sys

linhas = sys.stdin.read().splitlines()
for i in range(0, len(linhas), 2):
    dna = linhas[i]
    resistencia = linhas[i+1]
    print('Resistente' if resistencia in dna else 'Nao resistente')
