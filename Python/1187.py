ope = input()

soma = 0.0
for linha in range(12):
    for coluna in range(12):
        valor = float(input())
        if (linha != coluna and coluna > linha) and linha+coluna < 11:
            soma += valor
            
if ope == 'S':
    print(round(soma, 1))

else:
    print(round((soma/30), 1)) #30 é o número de casas na área superior