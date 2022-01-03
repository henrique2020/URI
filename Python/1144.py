valor = int(input())

for n1 in range(1, valor+1):
    for x in range(2):
        n2 = n1**2+x
        n3 = n1**3+x
        print('%d %d %d' % (n1, n2, n3))
