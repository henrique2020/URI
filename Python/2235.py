c1, c2, c3 = map(int, input().split())
if((c1 == c2) or (c2 == c3) or (c1 == c3)): print('S')
elif((c1+c2 == c3) or (c2+c3 == c1) or (c3+c1 == c2)): print('S')
else: print('N')
