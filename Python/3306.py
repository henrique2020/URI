from math import gcd

param, queries = map(int, input().split())
lista = list(map(int, input().split()))
for x in range(queries):
    try:
        dados = list(map(int, input().split()))
        posIni = dados[1]-1
        posFim = dados[2]
        if dados[0] == 1:
            for x in range(posIni, posFim):
                lista[x] += dados[3]
        else:
            print(gcd(*lista[posIni:posFim]))
    except:
        print(x+1)