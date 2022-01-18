while True:
    try: n = int(input())
    except: break

    lesmas = list(map(int, input().split()))
    vel = max(lesmas)
    if vel >= 20:
        print('3')
    elif vel < 10:
        print('1')
    else:
        print('2')
