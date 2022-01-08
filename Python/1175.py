arr = []
for x in range(20):
    arr.append(int(input()))

arr.reverse()
for x in range(20):
    print('N[%d] = %d' % (x, arr[x]))