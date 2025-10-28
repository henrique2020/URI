# Problema: 2466 - Sinuca      | Resposta: Accepted
# Linguagem: Python 3.11 [+1s] | Tempo: 0.001s

def geraDuplas(lista):
    return [[lista[p-1], lista[p]] for p in range(1, len(lista))]

input()
bolas = list(map(int, input().split()))
duplas = geraDuplas(bolas)
while len(duplas) > 1:
    bolas = [ 1 if d[0] == d[1] else -1 for d in duplas]
    duplas = geraDuplas(bolas)
    
print('preta' if duplas[0][0] == duplas[0][1] else 'branca')
