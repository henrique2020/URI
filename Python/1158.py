rep = int(input())
while rep:
    soma = 0
    ini, valores = map(int, input().split())
    if ini%2 != 0:
        soma+=ini
        ini+=2
        valores-=1
    else:
        ini+=1
    
    while valores:
        soma+=ini
        ini+=2
        valores-=1

    print(soma)
    rep-=1