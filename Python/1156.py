x = 1
exp = 1
for div in range(3, 40, 2):
    x+=div/2**exp
    exp+=1
print('{:.2f}'.format(x))
