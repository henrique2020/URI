from numpy.linalg import det

rep = int(input())
for raios in range(rep):
    x = []
    y = []
    z = []
    tiros = int(input())
    for posicao in range(tiros):
        pX, pY, pZ = input().split()
        x.append(int(pX)), y.append(int(pY)), z.append(int(pZ))

    matriz = [[x[0],y[0],z[0]], [x[1],y[1],z[1]]]
    for n in range(2, tiros):
        matriz.append([x[n],y[n],z[n]])
        print(matriz, det(matriz))
        del matriz[2]
    print()
