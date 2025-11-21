# Problema: 1593 - Função Binária | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]    | Tempo: 0.000s

for _ in range(int(input())):
    dec = int(input())
    number_bin = bin(dec)[2:]
    str_bin = str(number_bin)
    print(str_bin.count('1'))
