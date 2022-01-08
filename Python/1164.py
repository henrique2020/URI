rep = int(input())
while rep:
    soma = 0
    n = int(input())
    for x in range(1, n):
        if(n%x == 0):
            soma+=x

    if soma == n:
        print(f'{n} eh perfeito')
    else:
        print(f'{n} nao eh perfeito')
    rep-=1
