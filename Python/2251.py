while True:
    try: treinos = int(input())
    except: break

    media = 0
    dias = []
    for dia in range(1, treinos+1):
        tem, dis = map(int, input().split())
        med = dis/tem
        if(med > media):
            media = med
            dias.append(str(dia))
        
    print('\n'.join(dias))
