while 1:
    n = int(input())
    if n == 0:
        break
    v = list(map(int, input().split()))
    p = []
    for x in range(0, n):
        p.append(v[x]+v[-(1+x)])
    print(f'{max(p)} {min(p)}')
