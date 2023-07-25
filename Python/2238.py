# A -> DIVISOR
# B -> NÃO DIVISOR
# C -> MÚLTIPLO
# D -> NÃO MÚLTIPLO

def num_valido(n):
  return (n % A == 0 and C % n == 0) and (n % B != 0 and D % n != 0);


A, B, C, D = map(int, input().split())
n = C + 1
i = 1
while i * i <= C:
    if C % i == 0:
        if num_valido(i): n = min(n, i)             #Válida o I
        if num_valido(C // i): n = min(n, C // i)   #Válida o resultado da divisão
    i += 1

if n == C + 1: n = -1
print(n)