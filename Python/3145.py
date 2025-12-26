# Problema: 3145 - Uma Jornada Inesperada | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]            | Tempo: 0.000s

anoes, distancia = map(int, input().split())
print(f"{distancia/(anoes+2):.2f}")
