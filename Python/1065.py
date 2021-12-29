num = 5
p = 0
while (num):
    n = int(input())
    if(n%2 == 0):
        p+=1
    num-=1
print('%d valores pares' % p)
