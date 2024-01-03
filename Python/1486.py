while True:
    p, n, c = map(int, input().split())
    if(p == 0 and n == 0 and c == 0): break
    
    entradas = 0
    for _ in range(n):
        comprimento = sum(map(int, input().split()))
        if(comprimento >= c): entradas += 1
    
    print(entradas)
