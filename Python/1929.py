varetas = list(map(int, input().split()))
varetas.sort()
if(varetas[0]+varetas[1] > varetas[2]) or (varetas[1]+varetas[2] > varetas[3]): print('S')
else: print('N')
