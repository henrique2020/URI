for _ in range(int(input())):
    a, b = input().split()
    
    avancos = 0
    for p in range(len(a)):
        posicoes = ord(b[p]) - ord(a[p])
        if posicoes < 0: posicoes += 26
        avancos += posicoes
    
    print(avancos)