# Problema: 2044 - Em Dívida   | Resposta: Accepted
# Linguagem: Python 3.11 [+1s] | Tempo: 0.000s

while True:
    if int(input()) == -1: break

    visitas = total = 0
    for ingresso in list(map(int, input().split())):
        total += ingresso
        
        if total % 100 == 0:
            visitas += 1
            total = 0
        
    print(visitas)
