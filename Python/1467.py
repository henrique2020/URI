while True:
    try: a, b, c = input().split()
    except: break

    if a == b and b == c:
        print('*')
    elif a == b:
        print('C')
    elif b == c:
        print('A')
    else:
        print('B')
