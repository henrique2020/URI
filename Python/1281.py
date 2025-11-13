# Problema: 1281 - Ida à Feira | Resposta: Accepted
# Linguagem: Python 3.11 [+1s] | Tempo: 0.226s

for _ in range(int(input())):
    produtos = {}
    for _ in range(int(input())):
        p, v = input().split()
        produtos[p] = float(v)
    
    total = 0
    for _ in range(int(input())):
        p, q = input().split()
        total += produtos[p] * int(q)
        
    print(f"R$ {total:.2f}")
