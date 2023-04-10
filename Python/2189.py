caso = 0
while int(input()) != 0:
    caso += 1
    sequencia = list(map(int, input().split()))
    
    for i, v in enumerate(sequencia):
        if i+1 == v:
            vencedor = v
            break
    
    print('Teste', caso)
    print(vencedor)
    print()
