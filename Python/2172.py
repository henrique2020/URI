while(True):
    multiplicador, xp = map(int, input().split())
    
    if not multiplicador and not xp: break
    print(multiplicador*xp)
