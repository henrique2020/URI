# Problema: 2986 - Nem Tudo é Greve Versão Hard | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]                  | Tempo: 0.082s

memo = [1, 2, 4]
MOD = 10**9 + 7

degraus = int(input())

if degraus > len(memo):
    for i in range(3, degraus + 1):
        proximo = memo[i - 1] + memo[i - 2] + memo[i - 3]
        proximo %= MOD
        memo.append(proximo)

print(memo[degraus-1])
