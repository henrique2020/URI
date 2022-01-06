x=int(input())
while x:
    y=float(input())
    c=0
    while y>1:
        c+=1
        y/=2
    print('{} dias'.format(c))
    x-=1
