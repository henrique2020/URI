# Problema: 1244 - Ordenação por Tamanho | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]           | Tempo: 0.081s

[print(' '.join(sorted(input().split(), key=lambda palavra: len(palavra), reverse=True))) for _ in range(int(input()))]