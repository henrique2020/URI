# Problema: 2163 - O Despertar da Força | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]          | Tempo: 0.723s

def busca(n, m, mapa):
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if mapa[i][j] == '42':
                vizinhos = [
                    mapa[i-1][j-1], mapa[i-1][j], mapa[i-1][j+1],
                    mapa[i][j-1],                 mapa[i][j+1],
                    mapa[i+1][j-1], mapa[i+1][j], mapa[i+1][j+1]
                ]
                if vizinhos.count('7') == 8:
                    return i+1, j+1
    
    return 0, 0

n, m = map(int, input().split())
mapa = [input().split() for _ in range(n)]
print(' '.join(str(p) for p in busca(n, m, mapa)))