pos = int(input())
ope = input()

soma = 0.0
for linha in range(12):
    for coluna in range(12):
        valor = float(input())
        if coluna == pos:
            soma += valor

if ope == 'S':
    print(round(soma, 1))

else:
    print(round((soma/12), 1))
