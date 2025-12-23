# Problema: 1936 - Fatorial    | Resposta: Accepted
# Linguagem: Python 3.11 [+1s] | Tempo: 0.009s

objetivo = int(input())

memo = [1]
for i in range(1, objetivo):
    v = i * memo[i-1]
    if(v > objetivo): break
    memo.append(v)

valores = []
for v in sorted(memo, reverse=True):
    while sum(valores) + v <= objetivo:
        valores.append(v)
        if sum(valores) == objetivo:
            break     

print(len(valores))
