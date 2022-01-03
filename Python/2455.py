g = list(map(int, input().split()))
g1 = g[0]*g[1]
g2 = g[2]*g[3]
if g1 == g2:
    print('0')
elif g1 > g2:
    print('-1')
else:
    print('1')
