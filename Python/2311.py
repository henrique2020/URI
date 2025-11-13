# Problema: 2311 - Saltos Ornamentais | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]        | Tempo: 0.000s

for _ in range(int(input())):
    nome = input()
    dificuldade = float(input())
    notas = sorted(list(map(float, input().split())))
    total = sum(notas[1:len(notas)-1]) * dificuldade
    print(f"{nome} {total:.2f}")
