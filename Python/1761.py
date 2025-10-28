# Problema: 1761 - Decoração Natalina | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]        | Tempo: 0.073s

from math import tan
PI = 3.141592654

while True:
    try: angulo, distancia, altura_elfo = map(float, input().split())
    except: break
    
    angulo_convertido = angulo * PI / 180
    altura = tan(angulo_convertido) * distancia + altura_elfo
    print(f"{altura*5:.2f}")
