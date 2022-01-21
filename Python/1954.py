for x in range(int(input())):
    j1, ej1, j2, ej2 = input().split()
    nj1, nj2 = map(int, input().split())
    if((nj1+nj2)%2 == 0):
        if ej1 == 'PAR':
            print(j1)
        else:
            print(j2)
    else:
        if ej1 == 'IMPAR':
            print(j1)
        else:
            print(j2)