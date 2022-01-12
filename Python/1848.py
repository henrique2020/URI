x=3
arr=[]
while x:
    c=0
    while 1:
        y=input().replace('*','1').replace('-','0')
        if y=='caw caw':
            arr.append(c)
            x-=1
            break
        else:
            c+=int(y, 2)
print('\n'.join(map(str, arr)))
