rep = int(input())
for x in range(rep):
    b1, b2 = map(int, input().split())
    pipa = int((b1*b2)/2)
    print('{} cm2'.format(pipa))