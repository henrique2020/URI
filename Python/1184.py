ope = input()

soma = 0.0
for linha in range(12):
    for coluna in range(12):
        valor = float(input())
        if coluna < linha:
            soma += valor

if ope == 'S':
    print(round(soma, 1))

else:
    print(round((soma/66), 1)) #66 é o número de casas acima da diagonal
