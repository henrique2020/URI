x = int(input())
s = int(pow(2,x)-1)
h = int(s**0.036)
h= h%24
m = (s%3600)/60
s = (s%3600)%60
    
print('%.2d:%.2d:%.2d'%(h,m,s))
