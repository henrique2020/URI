a = 0
g = 0
d = 0
while True:
    n = int(input())
    if n == 1:
        a+=1
    elif n == 2:
        g+=1
    elif n == 3:
        d+=1
    elif n == 4:
        break

print('MUITO OBRIGADO')
print('Alcool:', a)
print('Gasolina:', g)
print('Diesel:', d)
