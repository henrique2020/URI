rep = int(input())
cq = 0
while(rep):
    line = list(map(int, input().split()))
    if line[0] > line[1]:
        cq += line[1]
    rep-=1
print(cq)
