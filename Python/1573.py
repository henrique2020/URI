# Problema: 1573 - Fábrica de Chocolate | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]          | Tempo: 0.118s

while True:
    a, b, c = map(int, input().split())
    if a == b and b == c and a == 0: break
    
    volume = a * b * c
    lado_cubo = volume ** (1/3) # Igual a raiz cúbica de volume
    print(int(lado_cubo))
