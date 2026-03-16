# Problema: 2174 - Coleção de Pomekon | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]        | Tempo: 0.000s

import sys

POKEMONS = 151

data = sys.stdin.read().splitlines()
capturas = set(data[1:])

print(f"Falta(m) {POKEMONS - len(capturas)} pomekon(s).")