from math import gcd

ini = list(map(int, input().split()))
lista = list(map(int, input().split()))
for x in range(ini[1]):
    dados = list(map(int, input().split()))
    posIni = dados[1]
    posFim = dados[2]
    if dados[0] == 1:
        for x in range(posIni-1, posFim):
            lista[x] += dados[3]
    else:
        temp = lista[posIni-1:posFim]
        temp.sort(reverse=True)
        for x in range(len(temp)):
            for y in range(x+1, len(temp)):
                mdc = gcd(temp[x], temp[y])
        print(mdc)
