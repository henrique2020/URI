while True:
    try: n1, n2 = map(int, input().split())
    except: break
    
    n1 = bin(n1).replace('0b', '')
    n2 = bin(n2).replace('0b', '')

    if len(n1) > len(n2): max_size = len(n1)
    else: max_size = len(n2)

    n1 = n1.zfill(max_size)
    n2 = n2.zfill(max_size)

    c = ''
    for p in range(max_size):
        if(n1[p] == n2[p]): c += '0'
        else: c += '1'

    print(int(c, 2))
