rep = int(input())
for x in range(rep):
    p1 = 0
    p2 = 0
    g1 = 0
    g2 = 0
    for x in range(2): 
        j = list(map(int, input().split(' x ')))
        if x == 0:
            t1 = j[0]
            t2 = j[1]
            g2 += t2*3
        else:
            t1 = j[1]
            g1 += t1*3
            t2 = j[0]

        if(t1>t2):
            p1+=3
        elif(t2>t1):
            p2+=3
        else:
            p1+=1
            p2+=1

    if p1 != p2:
        if p1>p2:
           resultado = 'Time 1'
        else:
            resultado = 'Time 2'
    else:
        if g1!= g2:
            if g1>g2:
               resultado = 'Time 1'
            else:
                resultado = 'Time 2'
        else:
            resultado = 'Penaltis'
    
    print(resultado)
