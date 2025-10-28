# Problema: 2868 - Errrou!     | Resposta: Accepted
# Linguagem: Python 3.11 [+1s] | Tempo: 0.000s

for _ in range(int(input())):
    n1, sinal, n2, _, resultado = input().split()
    n1, n2, resultado = map(int, [n1, n2, resultado])
    
    r = 0
    if sinal == '+': r = n1 + n2
    elif sinal == '-': r = n1 - n2
    elif sinal == 'x': r = n1 * n2
    
    print(f"E{'r'*abs(resultado-r)}ou!")
