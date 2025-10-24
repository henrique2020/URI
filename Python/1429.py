
// Problema: 1429 - Fatorial de Novo! | Resposta: Accepted
// Linguagem: Python 3.11 [+1s]       | Tempo: 1.217s

MAX_DIGITS = 5

fat = [1]
for p in range(2, MAX_DIGITS+1):
    fat.append(fat[-1] * p)
fat = fat[::-1]

while True:
    acm = input()
    
    if int(acm) == 0:
        break
    
    jump = MAX_DIGITS - len(acm)
    res = 0
    for p, n in enumerate(acm):
        res += fat[jump + p] * int(n)
        
    print(res)
