v = int(input())
num = 0
for x in range(1000):
    print('N[{}] = {}'.format(x, num))
    if num+1 == v:
        num = 0
    else:
        num+=1