x = int(input())
while True:
    z = int(input())
    if z > x:
        break
count = 1
soma = x
while True:
    x+=1
    count+=1
    soma+=x
    if soma > z:
        break
print(count)
