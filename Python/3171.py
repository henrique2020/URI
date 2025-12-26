# Problema: 3171 - Cordão de Led | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]   | Tempo: 0.000s

def busca(v):
    conectados.add(v)
    for con in conexoes:
        if v in con:
            vizinho = con[0] if con[1] == v else con[1]
            
            if vizinho not in conectados:
                busca(vizinho)

n, l = map(int, input().split())
conexoes = [sorted(map(int, input().split())) for _ in range(l)]

conectados = set()
busca(1)

if len(conectados) == n: print("COMPLETO")
else: print("INCOMPLETO")
