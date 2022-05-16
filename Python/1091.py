while True:
    rep = int(input())
    if rep == 0: break
    
    divisa_x, divisa_y = map(int, input().split())
    for x in range(rep):
        x, y = map(int, input().split())
        if x == divisa_x or y == divisa_y:
            print('divisa')
        elif x > divisa_x:
            if y > divisa_y: print('NE')
            else: print('SE')
        else:
            if y > divisa_y: print('NO')
            else: print('SO')