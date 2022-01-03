while True:
    n1, n2 = map(int, input().split())
    if(n1 == 0 or n2 == 0):
        break

    if(n1>0 and n2>0):
        q = 'primeiro'
    elif(n1<0 and n2>0):
        q = 'segundo'
    elif(n1<0 and n2<0):
        q = 'terceiro'
    else:
        q = 'quarto'
    
    print(q)
