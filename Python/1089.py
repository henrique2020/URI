# Problema: 1089 - Loop Musical | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]  | Tempo: 0.038s

while (int(input()) != 0):
    amostras = list(map(int, input().split()))
    amostras.append(amostras[0])
    
    picos = 0
    ondas = []
    for p in range(0, len(amostras)-1):
        if amostras[p] > amostras[p+1]: ondas.append("d")
        elif amostras[p] < amostras[p+1]: ondas.append("c")

    for o in range(len(ondas)-1, -1, -1):
        if ondas[o] != ondas[o-1]: picos += 1
            
    print(picos)
