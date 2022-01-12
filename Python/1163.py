import math
while 1:
    try:
        h=float(input())
    except:
        break
    p1,p2=list(map(int,input().split()))
    n=int(input())
    g=-9.80665
    t=0
    while n:
        a,v=list(map(float,input().split()))
        a=(2*3.14159*a)/360
        b=math.sin(a)*v
        r=math.sqrt(b**2-(4*h*(g/2)))
        t1=(-b+r)/g
        t2=(-b-r)/g
        if t2>t1:
            t=t2
        else:
            t=t1
        vx=math.cos(a)*v
        y=vx*t
        if y>=p1 and  y<=p2:
            print('%.5f -> DUCK'%y)
        else:
            print('%.5f -> NUCK'%y)
        n-=1
