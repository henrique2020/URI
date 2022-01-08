while True:
    rep = 5
    soma = 0
    n = int(input())
    if n == 0:
        break
    
    if n%2 == 0:
        soma+=n
        n+=2
        rep-=1
    else:
        n+=1
    
    while rep:
        soma+=n
        n+=2
        rep-=1

    print(soma)
    rep-=1