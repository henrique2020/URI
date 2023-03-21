varetas = list(map(int, input().split()))
varetas.sort()

if(abs(varetas[0] - varetas[1]) > abs(varetas[-2] - varetas[-1])): a, b, c = varetas[:3]
else: a, b, c = varetas[1:]

if(a+b>=c) and (b+c>=a) and (c+a>=b): print('S')
else: print('N')
