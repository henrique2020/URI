input()
rpm = list(map(int, input().split()))
queda = 0
v = rpm[0]
for x in rpm[1:]:
    if(v > x): 
        queda = rpm.index(x)+1
        break
    else: v = x

print(queda)
