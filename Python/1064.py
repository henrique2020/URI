num = 6
pos = 0
sum = 0
while (num):
    n = float(input())
    if(n>0):
        pos+=1
        sum+=n
    num-=1
print('%d valores positivos' % pos)
print('%.1f' % (sum/pos))
