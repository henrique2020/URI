while True:
    try: tam = int(input())+1
    except: break
    ini = tam/3
    fim = tam-ini
    for x in range(1, tam):
        for y in range(1, tam):
            if(2*x == tam and 2*y == tam):
                    print('4', end='')
            elif ((x >= ini and y >= ini) and (x <= fim and y <= fim)):
                print('1', end='')
            elif x == y:
                print('2', end='')
            elif x+y == tam:
                print('3', end='')
            else:
                print('0', end='')
        print()
    print()
