while True:
    try:
        int(input())
        lesmas = list(map(int, input().split()))
        lesmas.sort()
        
        if lesmas[-1] < 10: print(1)
        elif lesmas[-1] < 20: print(2)
        else: print(3)
        
    except: break
