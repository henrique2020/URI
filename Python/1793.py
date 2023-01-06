while (int(input()) != 0):
    tempos = list(map(int, input().split()))
    ativo = 10
    ultimo = tempos[0]
    for t in tempos[1:]:
        dif = ultimo+10
        if dif > t: ativo += 10 - (dif - t)
        else: ativo += 10
        
        ultimo = t
        
    print(ativo)
