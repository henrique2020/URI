x=int(input())
while x:
    s,c,r=map(int,input().split())
    v=list(map(int, input().split()))
    v.sort()
    for e in range(c):
        v[e]+=r
    t=0
    for e in v:
        t+=1/e
    print('%.2f'%t)
    x-=1
