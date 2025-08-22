# Problema: 2251 - Torres de Hanói  | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]      | Tempo: 0.000s

def torre(n):
    if n == 1:
        return 1
    return 1 + 2 * torre(n-1)

i = 1;
while True:
    n = int(input())
    if n == 0: break
    
    print(f"Teste {i}")
    print(torre(n), end="\n\n")
    i += 1
