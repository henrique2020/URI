# Problema: 1436 - Jogo do Tijolo | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]    | Tempo: 0.000s

for case in range(1, int(input())+1):
    linha = list(map(int, input().split()))
    print(f"Case {case}: {linha[int(linha[0]/2)+1]}")