func = int(input())
mesa = []
for x in range(func):
    mesa.append(x+1)

rep = int(input())
while rep:
    event = list(map(int, input().split()))
    if event[0] == 1:
        pos1 = mesa.index(event[1])
        pos2 = mesa.index(event[2])
        mesa[pos1] = event[2]
        mesa[pos2] = event[1]
    else:
        print(mesa.index(event[1]))
    rep-=1
