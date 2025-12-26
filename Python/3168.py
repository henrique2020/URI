# Problema: 3165 - Primos Gêmeos | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]   | Tempo: 0.001s


import math
def primo(num):
    if num%2 == 0 and num > 2: return False
    return all(num%i for i in range(3,int(math.sqrt(num))+1, 2))

n = int(input())
par = []

i = 0 if n%2 != 0 else 1
while len(par) == 0:
    nMenos = n - i
    ePrimo = primo(nMenos)

    if ePrimo and primo(nMenos - 2):
        par = [nMenos - 2, nMenos]
    else:
        i += 2

print(" ".join(map(str, sorted(par))))
