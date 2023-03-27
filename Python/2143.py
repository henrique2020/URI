while True:
    rep = int(input())
    if rep == 0: break
    
    for _ in range(rep):
        n = int(input())
        if n%2==0:
            print(n*2-2)
        else:
            print(n*2-1)
