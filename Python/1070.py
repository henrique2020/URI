num = int(input())
rep = 6
if num%2 != 0:
    print(num)
    rep -= 1

i = 1
while(rep):
    if((num+i)%2 != 0):
        print(num+i)
        rep-=1
    i+=1
