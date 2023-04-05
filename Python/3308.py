for _ in range(int(input())):
    entrada = list(map(int, input().split()))
    m = entrada[0]
    a = entrada[1:]
    
    if a.count(1) >= 2: print('X')
    elif m == 1 or a.count(1) == 0: print(0)
    else: print(1)
