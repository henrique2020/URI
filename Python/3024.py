# Problema: 3024 - Mountain Ranges | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]     | Tempo: 0.000s

_, distancia = map(int, input().split())
mirantes = list(map(int, input().split()))
mirantes.sort()

visitados = 0
atual = 1
for p in range(1, len(mirantes)):
    if mirantes[p] - mirantes[p-1] <= distancia: atual += 1
    else:
        if visitados < atual: visitados = atual
        atual = 1

if visitados < atual: visitados = atual
print(visitados)
