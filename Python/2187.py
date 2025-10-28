# Problema: 2187 - Bits Trocados | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]   | Tempo: 0.000s

teste = 0
while True:
    total = int(input())
    if total == 0: break
    else: teste += 1
    
    cedulas = []
    for valor in [50, 10, 5, 1]:
        if total >= valor:
            cedulas.append(total//valor)
            total -= valor * cedulas[-1]
        else:
            cedulas.append(0)

    print(f"Teste {teste}")
    print(" ".join([str(n) for n in cedulas]))
    print()
