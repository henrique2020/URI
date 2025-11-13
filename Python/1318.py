# Problema: 1318 - Bilhetes Falsos | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]     | Tempo: 0.132s

while True:
    casos = input()
    if casos == '0 0': break
    
    bilhetes = input().split()
    unicos = set(bilhetes)
    
    print(sum(1 for numero in unicos if bilhetes.count(numero) > 1))
