dia = int(input())
dim = map(int, input().split())
if dia <= min(dim): print('S')
else: print('N')
