# Problema: 1593 - Função Binária | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]    | Tempo: 0.000s

for _ in range(int(input())):
    dec = int(input())
    print(f'{dec:b}'.count('1'))
