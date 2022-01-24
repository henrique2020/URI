rep = int(input())
while rep:
    p1, p2 = input().split()
    if len(p2) > len(p1):
        c = len(p1)
        add = p2[c:]
    else:
        c = len(p2)
        add = p1[c:]
    comb = ''
    for x in range(c):
        comb+=p1[x]+p2[x]
    comb+=add
    print(comb)
    rep-=1
