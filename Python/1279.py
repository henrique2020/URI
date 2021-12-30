control = 0
while True:
    try:
        ano=int(input())
        if control != 0:
            print()
        t1=0
        t2=0
        if (ano%4==0 and ano%100!=0) or ano%400==0:
            print('This is leap year.')
            t2=1
            if ano%55==0:
                t1=1
        if ano%15==0:
            print('This is huluculu festival year.')
            t2=1
        if t1==1:
            print('This is bulukulu festival year.')
        elif t2==0:
            print('This is an ordinary year.')
    except:
        break
    control+=1
