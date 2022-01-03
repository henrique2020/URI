rep = float(input())
distancia = 0
while(rep):
    line = list(map(int, input().split()))
    distancia += line[0]*line[1]
    rep-=1
print(distancia)
